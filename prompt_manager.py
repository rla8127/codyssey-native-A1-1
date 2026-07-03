"""
나만의 프롬프트 관리 (Prompt Manager)

터미널에서 메뉴 번호를 입력해 프롬프트를 관리하는 콘솔 프로그램.
- 표준 라이브러리(json)만 사용하며, 기능별로 함수를 분리한다.
- 실행 중 추가한 프롬프트와 즐겨찾기 상태는 메모리에 유지된다. (종료 시 초기화)
"""

# 미리 정의된 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 기본 프롬프트 데이터 (이전 미션에서 작성한 프롬프트 3개 이상)
# 각 프롬프트: 제목(title), 내용(content), 카테고리(category), 즐겨찾기(favorite), 조회수(views)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": (
            "당신은 10년 경력의 전문 블로거입니다.\n"
            "주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.\n"
            "서론, 본론, 결론 구조를 갖추고,\n"
            "독자의 관심을 끄는 제목을 3개 제안해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": True,
        "views": 0,
    },
    {
        "title": "제품 썸네일 생성",
        "content": (
            "다음 제품의 매력적인 썸네일 이미지를 생성해주세요.\n"
            "밝고 깔끔한 배경, 제품이 중앙에 오도록 구도를 잡고,\n"
            "쇼핑몰 대표 이미지로 사용할 수 있는 고해상도 스타일로 만들어주세요."
        ),
        "category": "이미지 생성",
        "favorite": False,
        "views": 0,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": (
            "당신은 15년 경력의 IT 컨설턴트입니다.\n"
            "고객의 비즈니스 상황을 먼저 질문으로 파악한 뒤,\n"
            "기술 선택지와 장단점을 표로 정리해 실질적인 조언을 제공합니다."
        ),
        "category": "페르소나",
        "favorite": False,
        "views": 0,
    },
    {
        "title": "뉴스 요약 자동화",
        "content": (
            "다음 뉴스 기사를 3줄로 요약해주세요.\n"
            "핵심 사실, 배경, 시사점 순서로 정리하고,\n"
            "마지막에 관련 키워드 5개를 추출해주세요."
        ),
        "category": "자동화",
        "favorite": False,
        "views": 0,
    },
]


def show_menu():
    """메인 메뉴를 출력한다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def add_prompt():
    """준비 중"""
    print("준비 중입니다.")


def show_list():
    """준비 중"""
    print("준비 중입니다.")


def show_by_category():
    """준비 중"""
    print("준비 중입니다.")


def search_prompt():
    """준비 중"""
    print("준비 중입니다.")


def show_detail():
    """준비 중"""
    print("준비 중입니다.")


def manage_favorite():
    """준비 중"""
    print("준비 중입니다.")


def show_favorites():
    """준비 중"""
    print("준비 중입니다.")


def main():
    """프로그램 진입점. 메뉴를 반복해서 보여주고 입력을 처리한다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            manage_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 번호입니다. 메뉴에서 다시 선택해주세요.")


if __name__ == "__main__":
    main()
