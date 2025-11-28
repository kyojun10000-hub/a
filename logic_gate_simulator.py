"""
간단한 논리 게이트 시뮬레이터 (Tkinter)
한국 고등학생이 이해하기 쉽게 작성된 예제 코드입니다.
"""

import tkinter as tk


# 기본 논리 게이트 함수들 (0 또는 1 정수 반환)
def AND_gate(a, b):
    """AND 게이트: 두 입력이 모두 1일 때만 1"""
    return 1 if a == 1 and b == 1 else 0


def OR_gate(a, b):
    """OR 게이트: 두 입력 중 하나라도 1이면 1"""
    return 1 if a == 1 or b == 1 else 0


def NOT_gate(a):
    """NOT 게이트: 입력을 뒤집어서 0->1, 1->0"""
    return 1 if a == 0 else 0


def XOR_gate(a, b):
    """XOR 게이트: 서로 다를 때만 1 (기본 게이트로 구성)"""
    part1 = AND_gate(a, NOT_gate(b))
    part2 = AND_gate(NOT_gate(a), b)
    return OR_gate(part1, part2)


def update_output(label, value):
    """출력 라벨을 값(0/1)에 맞게 숫자와 배경색으로 업데이트"""
    label.config(text=str(value), bg="green" if value == 1 else "red")


def create_two_input_gate(frame, title, gate_function):
    """두 입력을 가지는 게이트 패널을 만든다."""
    title_label = tk.Label(frame, text=title, font=("Arial", 14, "bold"))
    title_label.pack(pady=(5, 10))

    inputs_frame = tk.Frame(frame)
    inputs_frame.pack(pady=5)

    var_a = tk.IntVar(value=0)
    var_b = tk.IntVar(value=0)

    # 입력 체크박스 (0은 해제, 1은 체크)
    check_a = tk.Checkbutton(inputs_frame, text="입력 A", variable=var_a)
    check_b = tk.Checkbutton(inputs_frame, text="입력 B", variable=var_b)
    check_a.grid(row=0, column=0, padx=5, pady=2)
    check_b.grid(row=0, column=1, padx=5, pady=2)

    output_label = tk.Label(frame, text="0", width=4, font=("Arial", 14, "bold"), bg="red", fg="white")
    output_label.pack(pady=(10, 5))

    def on_change():
        a_val = var_a.get()
        b_val = var_b.get()
        result = gate_function(a_val, b_val)
        update_output(output_label, result)

    # 체크박스를 누를 때마다 on_change 실행
    check_a.config(command=on_change)
    check_b.config(command=on_change)

    # 초기 출력 반영
    on_change()


def create_not_gate(frame):
    """하나의 입력을 가지는 NOT 게이트 패널을 만든다."""
    title_label = tk.Label(frame, text="NOT Gate", font=("Arial", 14, "bold"))
    title_label.pack(pady=(5, 10))

    inputs_frame = tk.Frame(frame)
    inputs_frame.pack(pady=5)

    var_a = tk.IntVar(value=0)

    check_a = tk.Checkbutton(inputs_frame, text="입력 A", variable=var_a)
    check_a.grid(row=0, column=0, padx=5, pady=2)

    output_label = tk.Label(frame, text="0", width=4, font=("Arial", 14, "bold"), bg="red", fg="white")
    output_label.pack(pady=(10, 5))

    def on_change():
        a_val = var_a.get()
        result = NOT_gate(a_val)
        update_output(output_label, result)

    check_a.config(command=on_change)
    on_change()


def main():
    """GUI를 준비하고 실행하는 메인 함수"""
    root = tk.Tk()
    root.title("논리 게이트 시뮬레이터")

    # 2x2 그리드에 배치할 프레임들
    and_frame = tk.LabelFrame(root, text="AND")
    or_frame = tk.LabelFrame(root, text="OR")
    not_frame = tk.LabelFrame(root, text="NOT")
    xor_frame = tk.LabelFrame(root, text="XOR")

    frames = [and_frame, or_frame, not_frame, xor_frame]
    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

    for frame, (row, col) in zip(frames, positions):
        frame.grid(row=row, column=col, padx=10, pady=10, ipadx=10, ipady=10, sticky="nsew")

    # 각 게이트 패널 생성
    create_two_input_gate(and_frame, "AND Gate", AND_gate)
    create_two_input_gate(or_frame, "OR Gate", OR_gate)
    create_not_gate(not_frame)
    create_two_input_gate(xor_frame, "XOR Gate", XOR_gate)

    # 창 크기 조절 시 프레임이 함께 늘어나도록 설정
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
