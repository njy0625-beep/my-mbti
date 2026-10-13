이전에 작성한 index.html을 실행하거나 확장할 수 있는 두 가지 방식의 main.py 코드입니다. 상황에 맞게 선택하여 사용하실 수 있습니다.

방법 1. 파이썬 기본 라이브러리 기반 서버 (추가 설치 불필요)
별도 패키지(pip) 설치 없이 파이썬만 설치되어 있다면 실행 즉시 브라우저를 열어 index.html을 띄워주는 스크립트입니다.

Python
import http.server
import socketserver
import webbrowser

PORT = 8000


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    """캐시 방지 헤더가 추가된 HTTP 요청 처리 클래스"""

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()


def run_server():
    url = f"http://localhost:{PORT}"
    print(f"포켓몬 MBTI 웹 서버가 시작되었습니다: {url}")
    print("종료하려면 Terminal에서 Ctrl+C를 누르세요.")

    # 자동으로 기본 웹 브라우저 열기
    webbrowser.open(url)

    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버를 종료합니다.")
            httpd.server_close()


if __name__ == "__main__":
    run_server()
