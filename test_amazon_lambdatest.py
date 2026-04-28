import asyncio
from playwright.async_api import async_playwright

LT_USERNAME = "daksh80002"
LT_ACCESS_TOKEN = "LT_1NO6WVd3PQiqhKYUHkRLJuKrYs4aatEgIO0lB2qwaYnPSQl"

LT_URL = f"wss://cdp.lambdatest.com/playwright?capabilities=%7B%22browserName%22%3A%22Chrome%22%2C%22browserVersion%22%3A%22latest%22%2C%22LT%3AOptions%22%3A%7B%22platform%22%3A%22Windows+10%22%2C%22build%22%3A%22Amazon+Parallel+Test%22%2C%22name%22%3A%22Amazon+Search+Test%22%2C%22user%22%3A%22{LT_USERNAME}%22%2C%22accessKey%22%3A%22{LT_ACCESS_TOKEN}%22%7D%7D"

async def search_and_add_to_cart(playwright, product_name):
    browser = await playwright.chromium.connect(LT_URL)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://www.amazon.com")
    await page.wait_for_timeout(2000)

    search_box = page.locator("input#twotabsearchtextbox")
    await search_box.fill(product_name)
    await search_box.press("Enter")
    await page.wait_for_timeout(2000)

    first_result = page.locator("div.s-result-item[data-component-type='s-search-result']").first
    await first_result.click()
    await page.wait_for_timeout(2000)

    try:
        price = await page.locator("span.a-price span.a-offscreen").first.inner_text()
    except:
        price = "Price not found"

    print(f"[{product_name}] Price: {price}")

    try:
        add_to_cart_btn = page.locator("input#add-to-cart-button")
        await add_to_cart_btn.click()
        await page.wait_for_timeout(2000)
        print(f"[{product_name}] Successfully added to cart!")
    except:
        print(f"[{product_name}] Could not add to cart (may require login or variant selection)")

    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        task1 = asyncio.create_task(search_and_add_to_cart(playwright, "iPhone"))
        task2 = asyncio.create_task(search_and_add_to_cart(playwright, "Samsung Galaxy"))

        await asyncio.gather(task1, task2)

        print("\nBoth tasks completed in parallel on LambdaTest!")

asyncio.run(main())
