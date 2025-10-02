#!/bin/bash
# Setup script for Command History Manager
# Run this to add convenient aliases to your shell

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/command_history.py"

echo "🔧 Command History Manager - Setup"
echo "===================================="
echo ""
echo "This will add aliases to your shell configuration."
echo "Script location: $SCRIPT_PATH"
echo ""

# Detect shell
if [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
    SHELL_NAME="bash"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
    SHELL_NAME="zsh"
else
    echo "❌ Unsupported shell. Please use bash or zsh."
    exit 1
fi

echo "Detected shell: $SHELL_NAME"
echo "Config file: $SHELL_RC"
echo ""

# Check if already configured
if grep -q "# Command History Manager aliases" "$SHELL_RC" 2>/dev/null; then
    echo "⚠️  Aliases already exist in $SHELL_RC"
    echo "Remove them manually if you want to reinstall."
    exit 0
fi

# Backup original config
cp "$SHELL_RC" "${SHELL_RC}.backup.$(date +%Y%m%d_%H%M%S)"
echo "✅ Backed up $SHELL_RC"

# Add aliases
cat >> "$SHELL_RC" << EOF

# Command History Manager aliases (added $(date))
alias ch='python3 $SCRIPT_PATH'
alias ch-add='python3 $SCRIPT_PATH add'
alias ch-list='python3 $SCRIPT_PATH list'
alias ch-search='python3 $SCRIPT_PATH search'
alias ch-undo='python3 $SCRIPT_PATH undo'
alias ch-redo='python3 $SCRIPT_PATH redo'
alias ch-stats='python3 $SCRIPT_PATH stats'

# Quick function to track last command with exit code
ch-track() {
    local exit_code=\$?
    local last_cmd=\$(history 1 | sed 's/^[ ]*[0-9]*[ ]*//')
    python3 $SCRIPT_PATH add "\$last_cmd" -e \$exit_code
}

# Alias to track command after execution
alias ch-t='ch-track'

EOF

echo "✅ Added aliases to $SHELL_RC"
echo ""
echo "📝 Available aliases:"
echo "  ch              - Main command (same as 'python3 command_history.py')"
echo "  ch-add          - Add command: ch-add \"git status\" -e 0"
echo "  ch-list         - List history: ch-list"
echo "  ch-search       - Search: ch-search git"
echo "  ch-undo         - Undo last command"
echo "  ch-redo         - Redo command"
echo "  ch-stats        - Show statistics"
echo "  ch-track        - Track last command with exit code"
echo "  ch-t            - Short for ch-track"
echo ""
echo "🔄 To activate now, run:"
echo "  source $SHELL_RC"
echo ""
echo "💡 Example workflow:"
echo "  git status      # Execute command"
echo "  ch-t            # Track it with exit code"
echo "  ch-list         # View history"
echo "  ch-search git   # Search for git commands"
echo ""
echo "✨ Setup complete!"
