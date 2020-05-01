class Puppy:
    n_puppies = 0

    # define __new__
    def __new__(cls):
        if cls.n_puppies < 10:
            cls.n_puppies += 1
            return object.__new__(cls)

        return f" You can't make more than {cls.n_puppies + 1}"
