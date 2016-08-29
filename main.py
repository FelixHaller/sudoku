import sys

class Field():
    def __init__(self, number):
        self.number = number
        self.is_solved = False
        self.value = None
        self.possibilities = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    def __str__(self):
        if self.is_solved:
            return str(" " + self.value)
        else:
            return str(" _")

    def remove_possibilities(self, numbers) -> bool:
        '''Removes all the numbers from the list of possible ones'''
        len_a = len(self.possibilities)
        self.possibilities = self.possibilities - set(numbers)
        len_b = len(self.possibilities)
        if len_b == 1:
            self.is_solved = True
            self.value = self.possibilities.pop()
        return len_a != len_b


class Sudoku():
    def __init__(self, filename):
        self.fields = [Field(x) for x in range(81)]
        self.filename = filename
        self.reset()

    def reset(self):
        '''Resets the Sudoku field'''
        try:
            with open(self.filename) as f:
                game = "".join(f.read().splitlines())
        except:
            print(
                "Error while reading sudoku file: '{}'".format(self.filename),
                file=sys.stdout)
            sys.exit(1)
        if len(game) != 81:
            print("The sudoku must consist of 81 characters")

        for i, char in enumerate(game):
            if char.isdigit():
                self.fields[i].is_solved = True
                self.fields[i].value = char

    def __str__(self):
        s = "----------------------------\n"
        for i, field in enumerate(self.fields, 1):
            if (i-1) % 9 == 0:
                # beginning of line
                s += "|"
            s += str(field)
            if i > 0 and i % 9 == 0:
                # end of line
                s += "|\n"
            elif i % 3 == 0:
                # line between blocks
                s += "|"
            else:
                # a whitespace between the numbers for better readablility
                s += " "
            if i % 27 == 0:
                s += "----------------------------\n"
        return s

    def get_row_for_field(self, field: Field):
        '''Returns all elements for the row the field is in.'''
        start = (field.number//9) * 9
        try:
            return self.fields[start:start+9]
        except IndexError:
            print("ungültiges Feld")
            sys.exit(1)

    def get_column_for_field(self, field: Field):
        '''Returns all elements for the column the field is in.'''
        col = []
        col_nr = field.number % 9
        try:
            # TODO: I think it can be optimized
            for f in self.fields:
                if f.number % 9 == col_nr:
                    col.append(f)
        except IndexError:
            print("ungültige Spalte")
            sys.exit(1)
        return col

    def get_square_for_field(self, field: Field):
        '''Returns the square the field is in.'''
        square = []

        col = (field.number % 9) // 3 * 3
        row = (field.number // 27) * 3
        start = 9 * row + col
        # add three lines with three fields building the square
        for i in range(3):
            for field in self.fields[start:start+3]:
                square.append(field)
            start += 9
        return(square)

    def solve(self):
        to_remove = set()
        progress = True
        while progress:
            progress = False
            for f in self.fields:
                if f.is_solved:
                    continue
                # check row for solved numbers
                for field in self.get_row_for_field(f):
                    if field.is_solved:
                        to_remove.add(field.value)
                # check column for solved numbers
                for field in self.get_column_for_field(f):
                    if field.is_solved:
                        to_remove.add(field.value)
                # check square for solved numbers
                for field in self.get_square_for_field(f):
                    if field.is_solved:
                        to_remove.add(field.value)

                # did there anything happen in this round?
                if f.remove_possibilities(to_remove):
                    progress = True
                to_remove.clear()


def main(argv):
    sudoku = Sudoku(argv[1])
    print("Original:\n" + str(sudoku))
    sudoku.solve()
    # for field in sudoku.get_square_for_field(8):
    #     print(field, end="")
    print("Solution:\n" + str(sudoku))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: python3 {0} <filename>".format(sys.argv[0]))
        sys.exit(1)
    sys.exit(main(sys.argv))
