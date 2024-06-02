def euclidean_distance(t1, t2):
    x1 = t1[0]
    y1 = t1[1]

    x2 = t2[0]
    y2 = t2[1]

    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2

    return (x + y) ** 1 / 2


def calculate_distances(points):
    distances = []
    for t1 in points:
        for t2 in points:
            if t1 == t2:
                continue
            distance = euclidean_distance(t1, t2)
            distances.append(distance)
    return distances


def find_min_distance(points):
    distances = calculate_distances(points)

    min_distance = distances[0]

    for distance in distances:
        if min_distance > distance:
            min_distance = distance

    print("distances:", distances)
    return min_distance


def find_min_distance_points(min_distance, points):
    min_distance_points = []
    for t1 in points:
        for t2 in points:
            if t1 == t2:
                continue
            distance = euclidean_distance(t1, t2)
            if distance == min_distance and [t2, t1] not in min_distance_points:
                min_distance_points.append([t1, t2])
    return min_distance_points


def main():
    points = ()

    print("########## WELCOME TO MIN DISTANCE CALCULATOR ##########")
    print("This app calculates distances between 2 or up to 10 points and get the shortest distance of 2 points")

    count_of_points = -1
    while type(count_of_points) != int or count_of_points <= 1 or count_of_points > 10:
        try:
            count_of_points = int(input("Please enter how many points you have:"))
        except ValueError:
            print("Please enter a number")

    for index in range(count_of_points):
        exit_code = -1
        while exit_code < 0:
            try:
                x = int(input(f"Enter x{index + 1}:"))
                y = int(input(f"Enter y{index + 1}:"))

                pair = (x, y)

                points = points + (pair,)
                print("points", points)
                exit_code = 0
            except ValueError:
                print("Please enter integer values")

    min_distance = find_min_distance(points)
    min_distance_points = find_min_distance_points(min_distance, points)

    print(f"Min distance is {min_distance}")

    print("These points have the minimum distance:")
    for point_pair, index in min_distance_points:
        print(f"{index} - {point_pair}")


if __name__ == '__main__':
    main()

