from genai_prompt_chain import GoogleGenAIChain

class AgreementAnalyzer:
    def __init__(self, agreement: str, prompts_file: str = 'base/prompts.txt'):
        self.agreement = agreement
        self.prompts = self._load_prompts(prompts_file)
        self.validation_score = None
        self.risk_assessment_score = None

    def _load_prompts(self, file_path: str):
        prompts = {}
        current_key = None
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('[') and line.endswith(']'):
                    current_key = line[1:-1]  # Get the key without brackets
                    prompts[current_key] = ""
                elif current_key:
                    prompts[current_key] += line + " "
        return prompts

    def summarize_agreement(self):
        summarization_model = GoogleGenAIChain(self.prompts["summarization_system_prompt"]).create_chain()
        summary = summarization_model.invoke({
            "input": f"{self.prompts['summarization_system_prompt']} Agreement: {self.agreement}"
        })
        return summary.content

    def validate_summary(self, summary: str):
        validator_model = GoogleGenAIChain(self.prompts["validator_system_prompt"]).create_chain()
        validation_results = validator_model.invoke({
            "input": f"Agreement:'{self.agreement}' work of the other agent:'{summary}' {self.prompts['validator_system_prompt']}"
        })
        self.validation_score = validation_results.content  # Save the score for easy access
        return self.validation_score

    def assess_risk(self, summary: str):
        risk_analyzer_model = GoogleGenAIChain(self.prompts["risk_analyzer_system_prompt"]).create_chain()
        risk_results = risk_analyzer_model.invoke({
            "input": summary
        })
        self.risk_assessment_score = risk_results.content  # Save the score for easy access
        return self.risk_assessment_score

    def perform_analysis(self):
        # Full end-to-end analysis
        summary = self.summarize_agreement()
        validation = self.validate_summary(summary)
        risk = self.assess_risk(summary)
        return {
            "summary": summary,
            "validation_score": validation,
            "risk_assessment_score": risk
        }

    def get_risk_score(self):
        return self.risk_assessment_score

    def get_validation_score(self):
        return self.validation_score
