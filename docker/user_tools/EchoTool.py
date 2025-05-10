from r2r import Tool, AggregateSearchResult

class EchoTool(Tool):
    """
    Kullanıcıdan bir string alır ve aynen geri döndürür.
    """

    def __init__(self):
        super().__init__(
            name="echo",
            description="Kullanıcıdan bir string alır ve aynen geri döndürür.",
            parameters={
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Geri döndürülecek mesaj.",
                    },
                },
                "required": ["message"],
            },
            results_function=self.execute,
            llm_format_function=None,
        )

    async def execute(self, message: str, *args, **kwargs):
        """
        Kullanıcıdan alınan mesajı aynen döndürür.
        """
        output_response = f"ECHOLANDI: {message}"
        result = AggregateSearchResult(
            generic_tool_result=output_response,
        )
        context = self.context
        if context and hasattr(context, "search_results_collector"):
            context.search_results_collector.add_aggregate_result(result)
        return result 