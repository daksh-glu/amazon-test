import asyncio
from playwright.async_api import async_playwright

async def search_and_add_to_cart(browser, product_name):
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

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        task1 = asyncio.create_task(search_and_add_to_cart(browser, "iPhone"))
        task2 = asyncio.create_task(search_and_add_to_cart(browser, "Samsung Galaxy"))

        await asyncio.gather(task1, task2)

        await browser.close()
        print("\nBoth tasks completed in parallel!")

asyncio.run(main())
