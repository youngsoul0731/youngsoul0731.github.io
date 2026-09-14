"""Generate the static homepage: python3 scripts/build_homepage.py.

Paper records are shared across research groups so cross-listed work stays in sync.
The generated index.html is committed and works both with and without Jekyll.
"""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def paper_card(key, paper):
    authors = escape(paper["authors"]).replace("Yuanshuo Zhang", "<strong>Yuanshuo Zhang</strong>")
    author_line = f'<p class="paper-authors">{authors}</p>' if authors else ""
    links = "\n".join(
        f'<a href="{escape(link["url"], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(link["label"])} <span aria-hidden="true">↗</span></a>'
        for link in paper["links"]
    )
    return f'''<article class="topic-item" data-paper="{escape(key)}">
      <a class="paper-image-link" href="{escape(paper['url'], quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="Read {escape(paper['name'])}">
        <img src="{escape(paper['image'], quote=True)}" class="topic-thumb" width="640" height="360" loading="lazy" decoding="async" alt="{escape(paper['name'])} research overview">
      </a>
      <div class="paper-content">
        <div class="paper-heading"><span class="paper-name">{escape(paper['name'])}</span><span class="badge">{escape(paper['venue'])}</span></div>
        <h4 class="paper-title"><a href="{escape(paper['url'], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(paper['title'])}</a></h4>
        {author_line}
        <p class="paper-summary">{escape(paper['summary'])}</p>
        <p class="paper-meta">{escape(paper['role'])}</p>
        <div class="links">{links}</div>
      </div>
    </article>'''


def build():
    data = json.loads((ROOT / "_data/research.json").read_text())
    groups = []
    for number, group in enumerate(data["groups"], 1):
        cards = "\n".join(paper_card(key, data["papers"][key]) for key in group["papers"])
        variant = " single-paper" if len(group["papers"]) == 1 else ""
        groups.append(f'''<article class="topic-card{variant}" id="{escape(group['id'])}" aria-labelledby="{escape(group['id'])}-title">
          <div class="topic-heading">
            <div class="topic-icon" aria-hidden="true">{number:02d}</div>
            <div><h3 id="{escape(group['id'])}-title">{escape(group['title'])}</h3><p class="topic-meta">{escape(group['description'])}</p></div>
          </div>
          <div class="topic-items">{cards}</div>
        </article>''')
    template = (ROOT / "_includes/homepage-template.html").read_text()
    assert template.count("<!-- RESEARCH_CARDS -->") == 1
    output = template.replace("<!-- RESEARCH_CARDS -->", "\n".join(groups))
    (ROOT / "index.html").write_text(output)
    print(f"Built index.html: {len(data['papers'])} papers, {len(groups)} research groups.")


if __name__ == "__main__":
    build()
