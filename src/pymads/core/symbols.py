class Symbol:
    """
    Represents a symbol in the assembler.

    Original Pascal structure: Similar to the label record in MADS
    """

    def __init__(self, name: str, value: int = 0, symbol_type: str = "L"):
        """
        Initialize a new symbol.

        Args:
            name: Symbol name
            value: Symbol value (address or constant)
            symbol_type: Symbol type ('L' for label, 'C' for constant, 'V' for variable)
        """
        self.name = name
        self.value = value
        self.type = symbol_type
        self.is_defined = False
        self.references = []


class SymbolTable:
    """
    Manages symbols and their values.

    Original Pascal implementation: Similar to the label handling in MADS
    """

    def __init__(self):
        self.symbols = {}  # Dictionary of symbols by name

    def add_symbol(self, name: str, value: int = 0, symbol_type: str = "L") -> Symbol:
        """
        Add a symbol to the table.

        Args:
            name: Symbol name
            value: Symbol value
            symbol_type: Symbol type

        Returns:
            The created Symbol object
        """
        symbol = Symbol(name, value, symbol_type)
        self.symbols[name] = symbol
        return symbol

    def get_symbol(self, name: str) -> Symbol:
        """
        Get a symbol by name.

        Args:
            name: Symbol name

        Returns:
            Symbol object

        Raises:
            KeyError: If symbol doesn't exist
        """
        return self.symbols[name]

    def symbol_exists(self, name: str) -> bool:
        """
        Check if a symbol exists.

        Args:
            name: Symbol name

        Returns:
            True if symbol exists, False otherwise
        """
        return name in self.symbols

    def define_symbol(self, name: str, value: int) -> Symbol:
        """
        Define a symbol's value.

        Args:
            name: Symbol name
            value: Symbol value

        Returns:
            The updated Symbol object

        Raises:
            KeyError: If symbol doesn't exist
        """
        symbol = self.symbols[name]
        symbol.value = value
        symbol.is_defined = True
        return symbol
