import sys

import variant_mod


def main():
    print("=== ТЕЛЕМЕТРИЯ ИСПЫТАТЕЛЬНОГО СТЕНДА ===")

    raw_rpm = [0, 450, 1495, 1502, 1498, 1500, 1505, 1100, 0]
    start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    end_idx = int(sys.argv[2]) if len(sys.argv) > 2 else 7

    if start_idx < 0 or end_idx < 0:
        print("Ошибка: индексы не должны быть отрицательными")
        return
    if start_idx > len(raw_rpm) or end_idx > len(raw_rpm):
        print("Ошибка: индекс выходит за границы списка")
        return
    if start_idx >= end_idx:
        print("Ошибка: начальный индекс должен быть меньше конечного")
        return
    filtered_rpm = variant_mod.filter_negative_spikes(raw_rpm)

    steady_rpm = variant_mod.trim_transient_process(
        filtered_rpm, start_idx, end_idx
    )

    telemetry = {"RPM": steady_rpm}
    stats = variant_mod.calculate_channel_stats(telemetry)
    print(f"Исходные данные: {raw_rpm}")
    print(f"После фильтрации: {filtered_rpm}")
    print(f"Установившийся режим: {steady_rpm}")
    print(f"Средняя частота: {stats['RPM']:.1f} об/мин")

if __name__ == "__main__":
    main()