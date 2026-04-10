"""
SBTI人格测试网站源码下载工具

功能：从SBTI测试网站下载完整的HTML源代码
网址：https://sbti.unun.dev
输出：01-源代码/网站源代码.html
"""

import urllib.request
from pathlib import Path


def download_website_source():
    """下载网站HTML源代码"""
    url = "https://sbti.unun.dev"
    output_dir = Path("../01-源代码")
    output_file = output_dir / "网站源代码.html"
    
    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"正在从 {url} 下载源代码...")
    
    try:
        # 设置请求头，模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # 创建请求
        request = urllib.request.Request(url, headers=headers)
        
        # 下载网页内容
        with urllib.request.urlopen(request, timeout=30) as response:
            html_content = response.read().decode('utf-8')
        
        # 保存到文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # 输出结果
        file_size = len(html_content) / 1024  # KB
        print(f"\n下载完成！")
        print(f"文件大小：{file_size:.1f} KB")
        print(f"保存位置：{output_file.absolute()}")
        
        return True
        
    except urllib.error.URLError as e:
        print(f"\n下载失败：网络错误")
        print(f"错误信息：{e}")
        return False
        
    except Exception as e:
        print(f"\n下载失败：{e}")
        return False


def main():
    print("=" * 60)
    print("SBTI人格测试网站源码下载工具")
    print("=" * 60)
    print()
    
    success = download_website_source()
    
    if success:
        print("\n提示：源代码已保存，可以使用浏览器打开查看")
    else:
        print("\n提示：下载失败，请检查网络连接或稍后重试")


if __name__ == "__main__":
    main()
