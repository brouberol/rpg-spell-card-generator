from dataclasses import dataclass

from dnd5e_card_generator.export.formatter import BaseCardTextFormatter
from dnd5e_card_generator.models import Card


@dataclass
class ClassFeature(BaseCardTextFormatter):
    class_name: str
    title: str
    text: list[str]
    lang: str

    @property
    def text_parts(self) -> str:
        return [self.format_text(part) for part in self.text]

    @property
    def contents_text(self) -> list[str]:
        return self.assemble_text_contents(
            self.format_title(title=self.title, icon="stars-stack"),
            self.format_spell_school("illusion"),
            self.format_header_separator(),
            self.text_parts,
        )

    def to_card(self) -> dict:
        card = Card(
            title=self.title,
            color="DarkCyan",
            icon=None,
            contents=self.contents_text,
        )
        return card.to_dict()
