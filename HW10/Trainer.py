from Consultant import Consultant


class Trainer(Consultant):
    def __init__(self, name: str, age: int, area_of_expertise: str, training_subject: str):
        super().__init__(name, age, area_of_expertise)
        self._training_subject = training_subject

    @property
    def training_subject(self):
        return self._training_subject

    @training_subject.setter
    def training_subject(self, new_training_subject):
        if isinstance(new_training_subject, str) and len(new_training_subject) < 15:
            self._training_subject = new_training_subject
        else:
            print(f'New training subject should be a string with length less than 15\n'
                  f'{type(new_training_subject)} with length {len(new_training_subject)} received instead')

    def conduct_training(self):
        print(f"{self.name} is conducting training on {self.training_subject}.")

    def work(self):
        print(f"{self.name} is performing training duties.")

if __name__ == '__main__':
    trainer = Trainer("Tom", 25, "Marketing", "Digital Marketing")
    trainer.conduct_training()
    trainer.training_subject = 'Trainer'
