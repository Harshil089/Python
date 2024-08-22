# Decorators for formatting options
def bold_decorator(func):
    def wrapper(*args, **kwargs):
        content = func(*args, **kwargs)
        return f"**{content}**"  # Bold formatting
    return wrapper

def italic_decorator(func):
    def wrapper(*args, **kwargs):
        content = func(*args, **kwargs)
        return f"*{content}*"  # Italic formatting
    return wrapper

def underline_decorator(func):
    def wrapper(*args, **kwargs):
        content = func(*args, **kwargs)
        return f"__{content}__"  # Underline formatting
    return wrapper

class Report:
    # Class-level default formatting
    default_formatting = []

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.format_options = []

    def add_formatting(self, decorator):
        self.format_options.append(decorator)

    def apply_formatting(self):
        formatted_content = self.content
        for decorator in self.format_options:
            formatted_content = decorator(lambda: formatted_content)()
        return formatted_content

    def __str__(self):
        formatted_content = self.apply_formatting()
        return f"Title: {self.title}\nContent: {formatted_content}"

    @classmethod
    def set_default_formatting(cls, decorator):
        cls.default_formatting.append(decorator)

    @classmethod
    def apply_default_formatting(cls, content):
        for decorator in cls.default_formatting:
            content = decorator(lambda: content)()
        return content

# Example usage
if __name__ == "__main__":
    # Create a report
    report = Report("Weekly Report", "This is the weekly performance report.")

    # Add dynamic formatting options
    report.add_formatting(bold_decorator)
    report.add_formatting(italic_decorator)

    # Print the formatted report
    print(report)

    # Apply and print with default formatting
    Report.set_default_formatting(underline_decorator)
    default_formatted_content = Report.apply_default_formatting("Default Formatting Applied Here")
    print(f"\nDefault Formatted Content:\n{default_formatted_content}")
