import logging


def multi(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        return "Error"


def multi2(a, b):
    return a * b


def check(users, age):
    count = 0
    for user in users:
        try:
            user_age = int(user["age"])
        except KeyError:
            print("Nieporawane dane: {}".format(user))
        except ValueError:
            print("Nieporawany wiek: {}".format(user))
        else:
            count += 1 if user_age < age else 0
        finally:
            print("Sprawdzono: {}".format(user))
    return count


def check2(users,age):
    return sum(1 for user in users if int(user["age"]) < age)


valid_data = [{"name": "Tom", "age": "10"},
              {"name": "Jack", "age": "20"},
              {"name": "Mary", "age": "30"}]
invalid_data = [{},
                {"name": "Jack", "age": "20"},
                {"name": "Mary", "age": "30"}]
invalid_data2 = [{"name": "Tom", "age": "age"},
                {"name": "Jack", "age": "20"},
                {"name": "Mary", "age": "30"}]

print(check(valid_data, 20))
# print(check(invalid_data, 20))
print(check(invalid_data2, 20))

# print(multi("2", "a"))

# try:
#     print(multi2("2", "3"))
# except TypeError:
#     logging.warning("Error")

# try:
#     print(multi2("2", "3"))
# except Exception as e:
#     print("Error:", e.with_traceback(None))
