from pathlib import Path


def search_index(markdown: Path, index: dict, query: str, limit: int = 5) -> dict:
    terms = [term.casefold() for term in query.split() if term.strip()]
    if not terms:
        return {"matches": []}

    lines = markdown.read_text(encoding="utf-8").splitlines()
    matches = []
    for section in index.get("sections", []):
        start = section["start_line"]
        end = section["end_line"]
        content_lines = lines[start - 1:end]
        content = "\n".join(content_lines)
        haystack = content.casefold()
        score = sum(1 for term in terms if term in haystack) / len(terms)
        if score:
            excerpt = _excerpt(content_lines, terms)
            matches.append({
                "section": section["id"],
                "score": round(score, 2),
                "lines": f"{start}-{end}",
                "excerpt": excerpt,
            })
    matches.sort(key=lambda item: item["score"], reverse=True)
    return {"matches": matches[:limit]}


def _excerpt(lines: list[str], terms: list[str]) -> str:
    for line in lines:
        folded = line.casefold()
        if any(term in folded for term in terms):
            return line.strip()[:240]
    return " ".join(line.strip() for line in lines[:3])[:240]
