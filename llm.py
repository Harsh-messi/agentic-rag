from transformers import pipeline

# Load a free model (runs locally)
# You can change model later if needed
generator = pipeline(
    "text-generation",
    model="gpt2",
    device=-1  # CPU (safe for your laptop)
)


def llm_call(prompt):
    try:
        # Limit input size (important for stability)
        prompt = prompt[:1000]

        response = generator(
            prompt,
            max_new_tokens=150,
            do_sample=True,
            temperature=0.3,
            top_p=0.9
        )

        output = response[0]["generated_text"]

        # Remove prompt from output (clean answer)
        answer = output[len(prompt):].strip()

        return answer if answer else "No meaningful answer generated."

    except Exception as e:
        return f"LLM Error (Free Model): {str(e)}"