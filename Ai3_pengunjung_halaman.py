import asyncio
from playwright.async_api import async_playwright

async def kunjungi_link(browser, url):
    try:
        # Membuka tab browser baru dengan penyamaran manusia
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            extra_http_headers={"Referer": "https://google.com"}
        )
        page = await context.new_page()
        
        print(f"🔄 [PROSES] Membuka halaman: {url}")
        
        # Membuka link dan menunggu halaman termuat total (JavaScript aktif)
        await page.goto(url, wait_until="networkidle", timeout=60000)
        
        # Jeda 5 detik di dalam halaman agar Google Apps Script sempat mencatat data
        await asyncio.sleep(5)
        print(f"✅ [SUKSES] Berhasil mengunjungi: {url}")
        
        await context.close()
    except Exception as e:
        print(f"❌ [GAGAL] Tidak dapat membuka {url}: {e}")

async def main():
    # 🎯 Silakan ganti 3 link target Anda di bawah ini
    daftar_url = [
        "https://topsitus.com/rtp-kingtoto",
        "https://topsitus.com/prediksi-s88",
        "https://topsitus.com/result-s88",
        "https://topsitus.com/rtp-suhutoto88",
        "https://topsitus.com/luckyspin-suhutoto88"
    ]
    
    async with async_playwright() as p:
        # Meluncurkan browser Chrome virtual (headless)
        browser = await p.chromium.launch(headless=True)
        
        # Membuka link secara berurutan satu per satu
        for indeks, url in enumerate(daftar_url):
            await kunjungi_link(browser, url)
            
            # Jika ini BUKAN link terakhir, berikan jeda waktu sebelum lanjut ke link berikutnya
            if indeks < len(daftar_url) - 1:
                menit_jeda = 10  # 💡 SEKARANG DIUBAH MENJADI 10 MENIT
                detik_jeda = menit_jeda * 60
                print(f"⏳ [JEDA] Menghentikan bot selama {menit_jeda} menit agar tidak terdeteksi spam...")
                await asyncio.sleep(detik_jeda)
        
        await browser.close()
        print("🎉 [SELESAI] Semua link telah sukses dikunjungi dengan aman!")

if __name__ == "__main__":
    asyncio.run(main())
