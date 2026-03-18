from ddgs import DDGS
from config.settings import DDG_REGION, DDG_MAX_RESULTS

def ddg_search(query: str) -> str:
    try:
        output = []
        with DDGS() as ddgs:
            results = ddgs.text(
                query = query, 
                region= DDG_REGION,
                max_results= DDG_MAX_RESULTS,
            )

            for i,r in enumerate(results, start=1):
                title = r.get("title", "")
                snnipet = r.get("body", "")
                link = r.get("href", "")
                output.append(f"{i}. {title}\n{snnipet}\n{link}\n")

        return "\n".join(output) if output else "No results found."

    except Exception as e:
        return f"Search in DuckDuckGo failed: {e}"