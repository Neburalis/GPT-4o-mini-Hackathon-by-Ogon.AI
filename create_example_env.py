def create_example_env(env_file_path='.env', example_env_file_path='example.env') -> None:
    """
        Creates an example environment file based on the variables from an existing .env file.

        Args:
            env_file_path (str): Path to the .env file containing environment variables. Default is '.env'.
            example_env_file_path (str): Path to the example environment file to be created or updated. Default is 'example.env'.

        Returns:
            None

        Raises:
            FileNotFoundError: If the .env file is not found.

        Example:
            create_example_env('.env', 'example.env')
        """
    # Reading variables from .env file
    try:
        with open(env_file_path, 'r') as env_file:
            lines = env_file.readlines()
    except FileNotFoundError:
        print(f"Error: {env_file_path} not found.")
        return

    header = """# This is a template for your environment variables file.
# Please replace the placeholder values with your actual secrets.
# Once updated, rename this file to .env and ensure it is not included in version control.

"""

    # Collecting contents for example.env file
    example_lines = [header]
    for line in lines:
        # Убираем пустые строки и комментарии
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('#'):
            if '=' in stripped_line:
                key, _ = stripped_line.split('=', 1)
                example_line = f"{key}=<your_{key.lower()}>\n"
                example_lines.append(example_line)

    # We write to the example.env file
    with open(example_env_file_path, 'w') as example_env_file:
        example_env_file.writelines(example_lines)

    print(f"Successfully created/updated {example_env_file_path}.")