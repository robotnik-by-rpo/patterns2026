from Src.Core.abc_data import unit
from Src.Core.validate import validate
from Src.Core.exception import arguments_exception
from Src.Models.recipe_line_model import recipe_line_model
from Src.Models.ingredient_model import ingredient_model
from Src.Models.package_model import package_model

class recipe_model(unit):
    """Recipe = information of dish + instruction of cooking"""

    __lines: list[recipe_line_model] = []
    __instruction: list[str] = []

    def __init__(self,
                 name: str,
                 lines: list[recipe_line_model],
                 instruction: list[str] = None):
        super().__init__()
        self.name = name
        self.lines = lines
        self.instruction = instruction if instruction is not None else []

    @property
    def lines(self) -> list[recipe_line_model]:
        """Getter for recipe lines"""
        return self.__lines

    @lines.setter
    def lines(self, new_lines: list[recipe_line_model]) -> None:
        """Setter for recipe lines"""
        self.__lines = validate.validated_null_empty_obj(
            new_lines,
            "new lines",
            "recipe must have at least one line",
            arguments_exception
        )

    @property
    def instruction(self) -> list[str]:
        """Getter for instruction"""
        return self.__instruction

    @instruction.setter
    def instruction(self, new_instruction: list[str]) -> None:
        """Setter for instruction"""
        self.__instruction = validate.validated_null_value(
            new_instruction,
            "new instruction",
            "new instruction must be not None",
            arguments_exception)

    @property
    def brutto(self) -> float:
        """Brutto recipe = sum of brutto all lines"""
        return sum(line.brutto for line in self.lines)

    @property
    def netto(self) -> float:
        """Netto recipe = sum of netto all lines"""
        return sum(line.netto for line in self.lines)

    @classmethod
    def create_recipe(cls) -> "recipe_model":

        ingredients = ingredient_model.create_ingredients()
        package = package_model.create_package_paper()
        lines = [
            recipe_line_model(ingredients[0], 187.5, 1.0),
            recipe_line_model(ingredients[1], 150.0, 1.0),
            recipe_line_model(ingredients[2], 3.0, 1.0),
            recipe_line_model(ingredients[3], 3.5, 1.0),
            recipe_line_model(package, 1.0, 1.0),    
        ]
        instruction = [
            "Отмеряем 300 мл воды и слегка подогреваем ее в микроволновке (прям чуть теплая должна быть, не выше 40С). Высыпаем пакетик сухих дрожжей (в США расфасовка в 7 гр., поэтому округлил для удобства. В оригинале 6 гр. сухих дрожжей или 12 гр. свежих). Хорошо размешиваем дрожжи в воде и оставляем на 5 минут.",
            "В эту же миску насыпаем 375 гр. муки и 7 гр. соли. Все это очень удобно делать с кухонными весами. Надеюсь, вы ими уже давно обзавелись.",
            "Осторожно вымешиваем тесто лопаточкой от краев к центру минут пять, больше не надо. Тесто получается очень липкое.",
            "Закрываем миску с тестом пищевой пленкой, делаем несколько наколов в пленке для циркуляции воздуха и ставим в теплое место на 1,5/2 часа. Тесто сильно увеличится в объеме.\nМожно дольше. Можно тесто подержать в тепле это время, затем убрать в холодильник на ночь, например, чтобы испечь багет с утра к завтраку.",
            "Включаем духовку на 240°С (465°F). На разделочный стол, припудренный мукой, вываливаем наше тесто. Аккуратно, не обминая, чтобы сохранить объем.\nНебольшое хауту: чтобы не пачкать мебель мукой и жиром, я всегда использую вощеную бумагу для работы с тестом. Просто отрываю пару полосок, провожу мокрой губкой по поверхности стола и кладу сверху вощеную бумагу. Бумага тогда не двигается и очень удобно раскатывать и вымешивать любое тесто. Потом эта бумага просто выкидывается и уборки на кухне на порядок меньше!",
            "Делим тесто пополам, стараясь не мять его. Аккуратно выкладываем в форму для багетов и распределяем вдоль ложбинок. Накрываем чистым полотенцем и оставляем до момента полного разогрева духовки (минут двадцать) - тесто за это время еще поднимется.",
            "Как только духовка разогрелась, ставим в самый ее низ поддон с ГОРЯЧЕЙ водой (ЭТО НЕОБХОДИМО!). Закрываем духовку на минут пять, чтобы она наполнилась паром. В это время обычными ножницами, бритвенным лезвием или острым ножом делаем косые надрезы на наших батончиках.\nСтавим форму с багетами в духовку на 25-35 минут, в зависимости от желаемой степени поджаристости корочки.",
            "Достаем форму из печи, перекладываем батоны на решетку для остывания. Оставляем их ничем не прикрывая минимум на 20 минут - багет должен дозреть."
        ]
        return cls("French baguette", lines, instruction)