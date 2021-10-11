import math

PAINT_FOR_10_METERS = 5
TIMES_FOR_10_METERS = 8
COST_PER_HOUR = 2000


def main():
    area = float(input("Введите площадь окрашиваемой поверхности: "))
    paint = float(input("Введите стоимость 5-литровой банки краски: "))

    paint_qty = get_paint_qty(area)
    job_hours = get_job_hours(area)
    paint_cost = get_paint_cost(paint, paint_qty)
    job_cost = get_job_cost(job_hours, COST_PER_HOUR)
    total_cost = paint_cost + job_cost

    print(f"На {area} м² потрбуется {paint_qty} банок краски и {job_hours} часов работы.")
    print(f"Стоимость краски составляет {format(paint_cost, '.2f')} грн.")
    print(f"Стоимость работы составляет {format(job_cost, '.2f')} грн.")
    print(f"Общая стоимость малярных работ - {format(total_cost, '.2f')} грн.")


def get_paint_qty(area):
    return math.ceil((area / 10 * PAINT_FOR_10_METERS) / 5)


def get_job_hours(area):
    return area / 10 * TIMES_FOR_10_METERS


def get_paint_cost(paint, paint_qty):
    return paint * paint_qty


def get_job_cost(job_hours, cost_per_hour):
    return job_hours * cost_per_hour


main()
