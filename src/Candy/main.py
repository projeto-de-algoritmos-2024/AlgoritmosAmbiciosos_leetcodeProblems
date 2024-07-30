from candy import Solution
def main():
    entrada = input("insira as ratings das crianças:")
    ratings_str = entrada.split()
    ratings = [int(rating) for rating in ratings_str]
    soma = Solution()
    print(soma.candy(ratings))
main()