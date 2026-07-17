"""
나만의 프롬프트 관리 (Prompt Manager) - Codyssey

터미널에서 메뉴 번호를 입력해 프롬프트를 관리하는 콘솔 프로그램.
- 표준 라이브러리(json)만 사용하며, 기능별로 함수를 분리한다.
- 실행 중 추가한 프롬프트와 즐겨찾기 상태는 메모리에 유지된다. (종료 시 초기화)
"""

import json
import os

# JSON 저장 파일 이름
DATA_FILE = "prompts.json"

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
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 조회수 Top 목록")
    print("11. JSON으로 저장")
    print("12. JSON에서 불러오기")
    print("13. 카테고리별 Markdown 내보내기")
    print("0. 종료")


def input_nonempty(label):
    """빈 값이 들어오면 다시 입력을 요청하는 공용 입력 함수."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("빈 값은 입력할 수 없습니다. 다시 입력해주세요.")


# 카테고리 직접 입력 시 자동 추가기능까진 구현안했음.
def select_category():
    """카테고리를 목록에서 선택하거나 직접 입력하도록 한다."""
    print("카테고리 선택:")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}) {name}")
    print(f"{len(CATEGORIES) + 1}) 직접 입력")

    while True:
        choice = input("선택: ").strip()
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(CATEGORIES):
                return CATEGORIES[num - 1]
            if num == len(CATEGORIES) + 1:
                return input_nonempty("카테고리 직접 입력: ")
        print("올바른 번호를 선택해주세요.")

# 1번 기능
def add_prompt():
    """새 프롬프트를 입력받아 리스트에 추가한다."""
    print("\n=== 프롬프트 추가 ===")
    title = input_nonempty("제목: ")
    content = input_nonempty("내용: ")
    category = select_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0,
    })
    print("프롬프트가 추가되었습니다!")

# 2번 기능
def show_list():
    """저장된 모든 프롬프트를 번호와 함께 출력한다."""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, item in enumerate(prompts, start=1):
        print(format_line(i, item))
    print(f"총 {len(prompts)}개의 프롬프트")


def format_line(index, item):
    """목록 한 줄 표기: '1. [카테고리] 제목 ⭐'"""
    star = " ⭐" if item["favorite"] else ""
    return f"{index}. [{item['category']}] {item['title']}{star}"

# 3번 기능
def show_by_category():
    """카테고리를 선택하면 해당 카테고리의 프롬프트만 출력한다."""
    print("\n=== 카테고리별 조회 ===")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}) {name}")

    choice = input("선택: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(CATEGORIES)):
        print("올바른 번호를 선택해주세요.")
        return

    category = CATEGORIES[int(choice) - 1]
    matched = [p for p in prompts if p["category"] == category]

    if not matched:
        print(f"[{category}] 카테고리에 등록된 프롬프트가 없습니다.")
        return

    print(f"\n[{category}] 카테고리 프롬프트:")
    for i, item in enumerate(matched, start=1):
        print(format_line(i, item))
    print(f"총 {len(matched)}개의 프롬프트")

# 4번 기능
def search_prompt():
    """키워드로 제목 또는 내용에 포함된 프롬프트를 검색한다."""
    print("\n=== 프롬프트 검색 ===")
    keyword = input_nonempty("검색어: ").lower()

    matched = [
        p for p in prompts
        if keyword in p["title"].lower() or keyword in p["content"].lower()
    ]

    if not matched:
        print("검색 결과가 없습니다.")
        return

    print("검색 결과:")
    for i, item in enumerate(matched, start=1):
        print(format_line(i, item))
    print(f"{len(matched)}개의 프롬프트를 찾았습니다.")

# 5번 기능
def show_detail():
    """번호를 입력하면 해당 프롬프트의 전체 내용을 출력한다. (조회수 증가)"""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    choice = input("번호 입력: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    item = prompts[int(choice) - 1]
    item["views"] += 1
    star = "⭐" if item["favorite"] else "없음"

    line = "─" * 28
    print(line)
    print(f"제목: {item['title']}")
    print(f"카테고리: {item['category']}")
    print(f"즐겨찾기: {star}")
    print(f"조회수: {item['views']}")
    print(line)
    print("내용:")
    print(item["content"])
    print(line)


def manage_favorite():
    """번호를 입력해 즐겨찾기를 추가/해제한다."""
    print("\n=== 즐겨찾기 관리 ===")
    print("즐겨찾기 토글 기능입니다. 중복 즐겨찾기 시 취소됩니다.")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, item in enumerate(prompts, start=1):
        print(format_line(i, item))

    choice = input("프롬프트 번호 입력: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    item = prompts[int(choice) - 1]
    item["favorite"] = not item["favorite"] # 토글
    if item["favorite"]:
        print(f"'{item['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"'{item['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")

# 7번 기능
def show_favorites():
    """즐겨찾기된 프롬프트만 모아서 출력한다."""
    print("\n=== 즐겨찾기 목록 ===")
    matched = [p for p in prompts if p["favorite"]]

    if not matched:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, item in enumerate(matched, start=1):
        print(format_line(i, item))
    print(f"총 {len(matched)}개의 즐겨찾기")


def edit_prompt():
    """번호를 입력해 프롬프트의 제목/내용/카테고리를 수정한다. (빈 입력은 기존값 유지)"""
    print("\n=== 프롬프트 수정 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, item in enumerate(prompts, start=1):
        print(format_line(i, item))

    choice = input("수정할 번호 입력: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    item = prompts[int(choice) - 1]
    print("(빈 값으로 두면 기존 내용을 유지합니다.)")
    new_title = input(f"제목 [{item['title']}]: ").strip()
    new_content = input("내용 (기존 유지하려면 Enter): ").strip()

    # 값이 있을 때만 교체
    if new_title:
        item["title"] = new_title
    if new_content:
        item["content"] = new_content

    change = input("카테고리를 변경할까요? (y/N): ").strip().lower()
    if change == "y":
        item["category"] = select_category()

    print("프롬프트가 수정되었습니다!")


def delete_prompt():
    """번호를 입력해 프롬프트를 삭제한다."""
    print("\n=== 프롬프트 삭제 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, item in enumerate(prompts, start=1):
        print(format_line(i, item))

    choice = input("삭제할 번호 입력: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    removed = prompts.pop(int(choice) - 1)
    print(f"'{removed['title']}' 프롬프트를 삭제했습니다.")


def show_top_views():
    """조회수 기준으로 정렬한 Top 목록을 출력한다."""
    print("\n=== 조회수 Top 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    ranked = sorted(prompts, key=lambda p: p["views"], reverse=True)
    for i, item in enumerate(ranked, start=1):
        print(f"{format_line(i, item)}  (조회수 {item['views']})")


def save_to_json():
    """현재 프롬프트 데이터를 JSON 파일로 저장한다. (보너스)"""
    print("\n=== JSON으로 저장 ===")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    print(f"'{DATA_FILE}' 파일에 {len(prompts)}개의 프롬프트를 저장했습니다.")


# prompts는 ㄹ
def load_from_json():
    """JSON 파일에서 프롬프트 데이터를 불러온다. (보너스)"""
    print("\n=== JSON에서 불러오기 ===")
    if not os.path.exists(DATA_FILE):
        print(f"'{DATA_FILE}' 파일이 없습니다. 먼저 저장해주세요.")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    prompts.clear()
    for item in loaded:
        item.setdefault("favorite", False)
        item.setdefault("views", 0)
        prompts.append(item)
    print(f"{len(prompts)}개의 프롬프트를 불러왔습니다.")


def export_markdown():
    """전체 프롬프트를 카테고리별 Markdown 파일로 내보낸다. (보너스)"""
    print("\n=== 카테고리별 Markdown 내보내기 ===")
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    export_dir = "prompts_export"
    os.makedirs(export_dir, exist_ok=True)

    categories = sorted({p["category"] for p in prompts})
    for category in categories:
        items = [p for p in prompts if p["category"] == category]
        # 파일 이름 공백, 슬래시 제거
        safe_name = category.replace(" ", "_").replace("/", "_")
        path = os.path.join(export_dir, f"{safe_name}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {category}\n\n")
            for item in items:
                star = " ⭐" if item["favorite"] else ""
                f.write(f"## {item['title']}{star}\n\n")
                f.write(f"{item['content']}\n\n")

    print(f"'{export_dir}/' 폴더에 {len(categories)}개 카테고리의 Markdown 파일을 생성했습니다.")


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
        elif choice == "8":
            edit_prompt()
        elif choice == "9":
            delete_prompt()
        elif choice == "10":
            show_top_views()
        elif choice == "11":
            save_to_json()
        elif choice == "12":
            load_from_json()
        elif choice == "13":
            export_markdown()
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 번호입니다. 메뉴에서 다시 선택해주세요.")


if __name__ == "__main__":
    main()
