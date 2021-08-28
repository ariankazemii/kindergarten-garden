class Garden:

    student = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny'
                        ,'Harriet', 'Ileana', 'Joseph', 'Kincaid' , 'Larry']
    
    plant = { 'C': 'Clover',
              'G': 'Grass',
              'R': 'Radishes',
              'V': 'Violets'}

    def __init__(self, diagram, students=student):
        self.diagram = diagram
        self.rows = [list(row) for row in diagram.split('\n')]
        self.plant_rows = [[self.plant[c] for c in row] for row in self.rows]
        self.students = sorted(students)

    def plants(self, name):
        return self.plants_for_index(self.students.index(name))


    def plants_for_index(self, i):
        return [self.plant_rows[0][i * 2],
                self.plant_rows[0][i * 2 + 1],
                self.plant_rows[1][i * 2],
                self.plant_rows[1][i * 2 + 1]]
