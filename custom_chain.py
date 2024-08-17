from langchain_core.prompts import ChatPromptTemplate


class TranslationChain:
    system_template = "Translate the following into {language}:"

    def __init__(self, model, parser):
        self.model = model
        self.parser = parser

    def language(self, language):
        prompt_template = ChatPromptTemplate.from_messages([
            ('system', self.system_template.format(language=language)),
            ('user', '{text}')
        ])

        chain = prompt_template | self.model | self.parser

        return chain
