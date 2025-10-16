#!/usr/bin/bash

# htop Source Compilation Script
# Day 12 Project: Compile htop from source with custom prefix
# Author: Yousif Elkot
# Date: October 16, 2025

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'    

WORK_DIR="$HOME/source_builds"
INSTALL_PREFIX="$HOME/.local"
HTOP_VERSION="3.3.0"
HTOP_URL="https://github.com/htop-dev/htop/releases/download/${HTOP_VERSION}/htop-${HTOP_VERSION}.tar.xz"

# function to print messages
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# check prerequisites
check_prerequisites() {
    print_info "Checking prerequisites..."
    
    local missing=()

    if ! command_exists gcc; then
        missing+=("gcc")
    fi

    if ! command_exists make; then
        missing+=("make")
    fi

    if [ ${#missing[@]} -ne 0 ]; then
        print_error "Missing required tools: ${missing[*]}"
        echo "Install with: sudo pacman -S base-devel (Arch) or sudo apt install build-essential (Debian/Ubuntu)"
        exit 1
    fi

    print_info "All prerequisites are met."
}

# create working directory
setup_workspace() {
    print_info "Setting up workspace at $WORK_DIR..."
    mkdir -p "$WORK_DIR"
    cd "$WORK_DIR" || { print_error "Failed to change directory to $WORK_DIR"; exit 1; }
}

# download source code
download_source() {
    print_info "Downloading htop version $HTOP_VERSION..."

    local tarball="htop-${HTOP_VERSION}.tar.xz"

    if [ -f "$tarball" ]; then
        print_warning "$tarball already exists. Skipping download."
    else
        if command_exists wget; then
            wget "$HTOP_URL" 
        elif command_exists curl; then
            curl -L -O "$HTOP_URL"
        else
            print_error "Neither wget nor curl is installed. Please install one to download files."
            exit 1
        fi
    fi

    print_info "Download completed."
}

# extract source code
extract_source() {
    print_info "Extracting source code..."

    local tarball="htop-${HTOP_VERSION}.tar.xz"
    local extrat_dir="htop-${HTOP_VERSION}"

    if [ -d "$extrat_dir" ]; then
        print_warning "$extrat_dir already exists, removing..."
        rm -rf "$extrat_dir"
    fi

    tar -xf "$tarball"
    cd "$extrat_dir" || { print_error "Failed to change directory to $extrat_dir"; exit 1; }
    print_info "Extraction completed."
    print_info "Source tree:"
    ls -lh
}

# configure build
configure_build() {
    print_info "Configuring the build with prefix $INSTALL_PREFIX..."

    if [ ! -f "configure" ]; then
        print_error "Configure script not found!"
        exit 1
    fi

    # run configure with custom prefix
    ./configure --prefix="$INSTALL_PREFIX" 2>&1 | tee configure.log

    if [ ${PIPESTATUS[0]} -ne 0 ]; then
        print_error "Configuration failed. Check configure.log for details."
        exit 1
    fi

    print_info "Configuration completed."
}

# compile source
compile_source() {
    print_info "Compiling the source code..."

    local cores=$(nproc 2>/dev/null || echo 2)
    print_info "Using $cores parallel jobs"

    make -j"$cores" 2>&1 | tee build.log

    if [ ${PIPESTATUS[0]} -ne 0 ]; then
        print_error "Compilation failed. Check build.log for details."
        exit 1
    fi

    print_info "Compilation completed."
}

# install compiled binary
install_binary() {
    print_info "Installing htop to $INSTALL_PREFIX..."

    make install 2>&1 | tee install.log

    if [ ${PIPESTATUS[0]} -ne 0 ]; then
        print_error "Installation failed. Check install.log for details."
        exit 1
    fi

    print_info "Installation completed."
}

# verify installation
verify_installation() {
    print_info "Verifying installation..."

    local htop_bin="$INSTALL_PREFIX/bin/htop"

    if [ ! -f "$htop_bin" ]; then
        print_error "htop binary not found at $htop_bin"
        exit 1
    fi

    print_info "htop binary found at $htop_bin"

    #check if it's in PATH
    if command_exists htop && [ "$(command -v htop)" = "$htop_bin" ]; then
        print_info "htop is correctly installed and in your PATH."
    else
        print_warning "htop is NOT in your PATH"
        echo ""
        echo "To add it to your PATH, add the following line to your shell profile (~/.bashrc, ~/.zshrc, etc.):"
        echo "export PATH=\"$INSTALL_PREFIX/bin:\$PATH\""
    fi

    #display version
    print_info "htop version:"
    $htop_bin --version
}

# generate summary report 
# Generate summary report
generate_report() {
    print_info "Generating compilation report..."
    
    local report_file="$WORK_DIR/htop_compilation_report.txt"
    
    cat > "$report_file" << EOF
HTOP Compilation Report
======================
Date: $(date)
Version: $HTOP_VERSION
Installation Prefix: $INSTALL_PREFIX

Build Details:
--------------
Working Directory: $WORK_DIR/htop-$HTOP_VERSION
Binary Location: $INSTALL_PREFIX/bin/htop

Compilation Steps:
1. ✓ Prerequisites checked
2. ✓ Source downloaded
3. ✓ Source extracted
4. ✓ Build configured
5. ✓ Source compiled
6. ✓ Binary installed
7. ✓ Installation verified

Files Created:
- configure.log (configuration output)
- compile.log (compilation output)
- install.log (installation output)

Next Steps:
-----------
1. Test htop: $INSTALL_PREFIX/bin/htop
2. Add to PATH if needed
3. Compare with system htop (if installed)

Notes:
------
This htop was compiled with custom optimizations for your system.
Source code is preserved at: $WORK_DIR/htop-$HTOP_VERSION
EOF
    
    cat "$report_file"
    print_info "Report saved to: $report_file"
}

# main script execution
main() {
    echo "=================================="
    echo "htop Source Compilation Script"
    echo "=================================="
    echo ""

    check_prerequisites
    setup_workspace
    download_source
    extract_source
    configure_build
    compile_source
    install_binary
    verify_installation
    generate_report

    echo ""
    print_info "🎉 htop compilation complete!"
    echo ""
    print_info "Try running: $INSTALL_PREFIX/bin/htop"
}

# run main
main