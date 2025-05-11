from r2r import Tool, AggregateSearchResult

class SecretMethodTool(Tool):
    """
    A user defined tool.
    """

    def __init__(self):
        super().__init__(
            name="secret_method",
            description="Performs a secret method.",
            parameters={
                "type": "object",
                "properties": {
                    "number": {
                        "type": "string",
                        "description": "An integer input for the secret method.",
                    },
                    "string": {
                        "type": "string",
                        "description": "A string input for the secret method.",
                    },
                },
                "required": ["number", "string"],
            },
            results_function=self.execute,
            llm_format_function=None,
        )

    async def execute(self, number: str, string: str, *args, **kwargs):
        """
        Implementation of the tool.
        """

        number_int = int(number)
        output_response = f"Your order for {number_int} dancing flamingos has been received. They will arrive by unicycle courier within 3-5 business dreams. Please prepare {string} for them."

        result = AggregateSearchResult(
            generic_tool_result=output_response,
        )

        context = self.context
        # Add to results collector if context is provided
        if context and hasattr(context, "search_results_collector"):
            context.search_results_collector.add_aggregate_result(result)

        return result
