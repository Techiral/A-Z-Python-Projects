import re
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ScriptRule:
    pattern: str
    replacement: str

class AncientScriptTranslator:
    def __init__(self):
        self.scripts: Dict[str, List[ScriptRule]] = {
            "linear_b": [
                ScriptRule(r"𐀀", "a"),
                ScriptRule(r"𐀁", "e"),
                ScriptRule(r"𐀂", "i"),
                ScriptRule(r"𐀃", "o"),
                ScriptRule(r"𐀄", "u"),
                # Add more Linear B characters and their translations
            ],
            "cuneiform": [
                ScriptRule(r"𒀀", "a"),
                ScriptRule(r"𒁀", "bi"),
                ScriptRule(r"𒂠", "ka"),
                ScriptRule(r"𒃠", "ga"),
                ScriptRule(r"𒅆", "mu"),
                # Add more cuneiform characters and their translations
            ],
            "hieroglyphs": [
                ScriptRule(r"𓂋", "r"),
                ScriptRule(r"𓃀", "b"),
                ScriptRule(r"𓅓", "m"),
                ScriptRule(r"𓈖", "n"),
                ScriptRule(r"𓊃", "s"),
                # Add more hieroglyph characters and their translations
            ]
        }

    def translate(self, text: str, script: str) -> str:
        if script not in self.scripts:
            raise ValueError(f"Unsupported script: {script}")

        translated = text
        for rule in self.scripts[script]:
            translated = re.sub(rule.pattern, rule.replacement, translated)
        return translated

    def add_rule(self, script: str, pattern: str, replacement: str):
        if script not in self.scripts:
            self.scripts[script] = []
        self.scripts[script].append(ScriptRule(pattern, replacement))

    def remove_rule(self, script: str, pattern: str):
        if script in self.scripts:
            self.scripts[script] = [rule for rule in self.scripts[script] if rule.pattern != pattern]

# Example usage
translator = AncientScriptTranslator()

linear_b_text = "𐀀𐀁𐀂𐀃𐀄"
print(f"Linear B: {linear_b_text}")
print(f"Translated: {translator.translate(linear_b_text, 'linear_b')}")

cuneiform_text = "𒀀𒁀𒂠𒃠𒅆"
print(f"Cuneiform: {cuneiform_text}")
print(f"Translated: {translator.translate(cuneiform_text, 'cuneiform')}")

hieroglyphs_text = "𓂋𓃀𓅓𓈖𓊃"
print(f"Hieroglyphs: {hieroglyphs_text}")
print(f"Translated: {translator.translate(hieroglyphs_text, 'hieroglyphs')}")

# Adding a new rule
translator.add_rule("linear_b", r"𐀅", "jo")
print(f"Translated with new rule: {translator.translate('𐀀𐀁𐀂𐀃𐀄𐀅', 'linear_b')}")
