from firecrawl import FirecrawlApp


app = FirecrawlApp(api_key="")

crawl_result = app.crawl_url('mendable.ai', {'crawlerOptions': {'excludes': ['blog/*']}},wait_until_done=False)
print(crawl_result)

job_id = crawl_result['jobId']
print(job_id)

status = app.check_crawl_status(job_id)
print(status)
