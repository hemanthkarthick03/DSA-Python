# Linux Commands Cheatsheet - Complete Guide with Best Practices

## Table of Contents
- [File System Navigation](#file-system-navigation)
- [File and Directory Operations](#file-and-directory-operations)
- [File Permissions](#file-permissions)
- [Text Processing](#text-processing)
- [Process Management](#process-management)
- [System Information](#system-information)
- [Network Commands](#network-commands)
- [Archive and Compression](#archive-and-compression)
- [Package Management](#package-management)
- [System Administration](#system-administration)
- [Monitoring and Performance](#monitoring-and-performance)
- [Security Commands](#security-commands)
- [Best Practices](#best-practices)

## File System Navigation

### Basic Navigation
```bash
# Print working directory
pwd

# List directory contents
ls                    # Basic listing
ls -l                 # Long format with details
ls -la                # Include hidden files
ls -lh                # Human readable file sizes
ls -lt                # Sort by modification time
ls -lS                # Sort by file size
ls -R                 # Recursive listing

# Change directory
cd /path/to/directory # Absolute path
cd ../                # Parent directory
cd ~                  # Home directory
cd -                  # Previous directory
cd                    # Home directory (shortcut)

# Directory shortcuts
.                     # Current directory
..                    # Parent directory
~                     # Home directory
/                     # Root directory
```

### Advanced Navigation
```bash
# Find files and directories
find /path -name "filename"           # Find by name
find /path -type f -name "*.txt"      # Find text files
find /path -type d -name "dirname"    # Find directories
find /path -size +100M                # Files larger than 100MB
find /path -mtime -7                  # Modified in last 7 days
find /path -user username             # Files owned by user

# Locate files (faster than find)
locate filename                       # Find files by name
updatedb                             # Update locate database

# Which command location
which command                        # Show command path
whereis command                      # Show command, source, manual paths
type command                         # Show command type and location
```

## File and Directory Operations

### Creating Files and Directories
```bash
# Create files
touch filename                       # Create empty file
touch file1 file2 file3             # Create multiple files
echo "content" > filename            # Create file with content
cat > filename                       # Create file and enter content

# Create directories
mkdir dirname                        # Create directory
mkdir -p path/to/nested/dir         # Create nested directories
mkdir dir1 dir2 dir3                # Create multiple directories
mkdir -m 755 dirname                # Create with specific permissions
```

### Copying and Moving
```bash
# Copy files and directories
cp source destination                # Copy file
cp -r source_dir dest_dir           # Copy directory recursively
cp -p source destination            # Preserve permissions and timestamps
cp -u source destination            # Copy only if source is newer
cp -v source destination            # Verbose output
cp -i source destination            # Interactive (prompt before overwrite)

# Move and rename
mv source destination                # Move/rename file or directory
mv file1 file2 file3 directory/     # Move multiple files to directory
mv -i source destination            # Interactive mode
mv -u source destination            # Move only if source is newer
```

### Removing Files and Directories
```bash
# Remove files
rm filename                          # Remove file
rm -i filename                       # Interactive removal
rm -f filename                       # Force removal (no prompts)
rm -v filename                       # Verbose output
rm *.txt                            # Remove all .txt files

# Remove directories
rmdir dirname                        # Remove empty directory
rm -r dirname                        # Remove directory and contents
rm -rf dirname                       # Force remove directory and contents
rm -ri dirname                       # Interactive recursive removal

# Safe removal practices
alias rm='rm -i'                     # Always prompt before deletion
trash filename                       # Use trash instead of rm (if available)
```

### Linking Files
```bash
# Hard links
ln source_file link_name             # Create hard link

# Symbolic links
ln -s source_file link_name          # Create symbolic link
ln -sf source_file link_name         # Force create symbolic link
readlink link_name                   # Show link target
ls -l                               # Shows link targets in listing
```

## File Permissions

### Understanding Permissions
```bash
# Permission format: rwxrwxrwx (owner, group, others)
# r = read (4), w = write (2), x = execute (1)

# View permissions
ls -l filename                       # Show detailed permissions
stat filename                       # Show detailed file information

# Change permissions
chmod 755 filename                   # rwxr-xr-x
chmod 644 filename                   # rw-r--r--
chmod +x filename                    # Add execute permission
chmod -w filename                    # Remove write permission
chmod u+x filename                   # Add execute for owner
chmod g-w filename                   # Remove write for group
chmod o+r filename                   # Add read for others
chmod -R 755 directory              # Recursive permission change
```

### Ownership
```bash
# Change ownership
chown user filename                  # Change owner
chown user:group filename            # Change owner and group
chown -R user:group directory        # Recursive ownership change
chgrp group filename                 # Change group only

# Special permissions
chmod u+s filename                   # Set SUID bit
chmod g+s filename                   # Set SGID bit
chmod +t directory                   # Set sticky bit
```

## Text Processing

### Viewing File Contents
```bash
# Display file contents
cat filename                         # Display entire file
cat -n filename                      # Display with line numbers
cat -b filename                      # Number non-blank lines
tac filename                         # Display in reverse order

# Paginated viewing
less filename                        # View file page by page
more filename                        # View file page by page (basic)
head filename                        # First 10 lines
head -n 20 filename                  # First 20 lines
tail filename                        # Last 10 lines
tail -n 20 filename                  # Last 20 lines
tail -f filename                     # Follow file changes (real-time)
```

### Text Searching and Filtering
```bash
# Search within files
grep "pattern" filename              # Search for pattern
grep -i "pattern" filename           # Case-insensitive search
grep -r "pattern" directory          # Recursive search
grep -n "pattern" filename           # Show line numbers
grep -v "pattern" filename           # Invert match (exclude pattern)
grep -c "pattern" filename           # Count matches
grep -l "pattern" *.txt              # List files containing pattern
grep -E "pattern1|pattern2" file     # Extended regex (OR)

# Advanced grep
grep -A 3 "pattern" filename         # Show 3 lines after match
grep -B 3 "pattern" filename         # Show 3 lines before match
grep -C 3 "pattern" filename         # Show 3 lines around match
grep -w "word" filename              # Match whole words only
```

### Text Manipulation
```bash
# Sort and unique
sort filename                        # Sort lines alphabetically
sort -n filename                     # Numeric sort
sort -r filename                     # Reverse sort
sort -k 2 filename                   # Sort by second column
uniq filename                        # Remove duplicate lines
sort filename | uniq                 # Sort and remove duplicates
sort filename | uniq -c              # Count occurrences

# Cut and paste
cut -d',' -f1 filename              # Extract first field (CSV)
cut -c1-10 filename                 # Extract characters 1-10
paste file1 file2                   # Merge files side by side

# Text replacement
sed 's/old/new/' filename           # Replace first occurrence per line
sed 's/old/new/g' filename          # Replace all occurrences
sed -i 's/old/new/g' filename       # In-place replacement
sed -n '1,5p' filename              # Print lines 1-5
```

### Advanced Text Processing
```bash
# AWK for text processing
awk '{print $1}' filename           # Print first column
awk -F',' '{print $2}' filename     # Use comma as delimiter
awk '{sum+=$1} END {print sum}' file # Sum first column
awk 'length($0) > 80' filename      # Lines longer than 80 characters

# Word and character count
wc filename                          # Lines, words, characters
wc -l filename                       # Count lines only
wc -w filename                       # Count words only
wc -c filename                       # Count characters only

# Compare files
diff file1 file2                     # Show differences
diff -u file1 file2                  # Unified diff format
cmp file1 file2                      # Compare files byte by byte
comm file1 file2                     # Compare sorted files
```

## Process Management

### Viewing Processes
```bash
# Process listing
ps                                   # Show current user processes
ps aux                              # Show all processes (detailed)
ps -ef                              # Show all processes (different format)
ps -u username                      # Show processes for specific user
ps -C command_name                  # Show processes by command name

# Real-time process monitoring
top                                 # Interactive process viewer
htop                                # Enhanced process viewer (if installed)
top -u username                     # Show processes for specific user
```

### Process Control
```bash
# Background and foreground
command &                           # Run command in background
jobs                               # List background jobs
fg %1                              # Bring job 1 to foreground
bg %1                              # Send job 1 to background
nohup command &                    # Run command immune to hangups

# Process termination
kill PID                           # Terminate process by PID
kill -9 PID                        # Force kill process
kill -TERM PID                     # Graceful termination
killall command_name               # Kill all processes by name
pkill pattern                      # Kill processes matching pattern
pgrep pattern                      # Find process IDs by pattern
```

### Process Monitoring
```bash
# System load and uptime
uptime                             # System uptime and load
w                                  # Who is logged in and what they're doing
who                                # Show logged in users
last                               # Show login history

# Process trees
pstree                             # Show process tree
pstree -p                          # Show process tree with PIDs
```

## System Information

### Hardware Information
```bash
# CPU information
lscpu                              # CPU architecture info
cat /proc/cpuinfo                  # Detailed CPU information
nproc                              # Number of processing units

# Memory information
free -h                            # Memory usage (human readable)
cat /proc/meminfo                  # Detailed memory information
vmstat                             # Virtual memory statistics

# Disk information
df -h                              # Disk space usage (human readable)
du -h directory                    # Directory size (human readable)
du -sh *                           # Size of all items in current directory
lsblk                              # List block devices
fdisk -l                           # List disk partitions (requires root)
```

### System Status
```bash
# System information
uname -a                           # System information
hostnamectl                        # System hostname and related info
timedatectl                        # System time and date settings
locale                             # System locale settings

# Kernel and modules
uname -r                           # Kernel version
lsmod                              # List loaded kernel modules
modinfo module_name                # Module information
dmesg                              # Kernel ring buffer messages
dmesg | tail                       # Recent kernel messages
```

### Environment Variables
```bash
# View environment variables
env                                # Show all environment variables
printenv                           # Show all environment variables
echo $PATH                         # Show specific variable
export VAR=value                   # Set environment variable
unset VAR                          # Remove environment variable

# Shell variables
set                                # Show all shell variables
declare -x VAR=value               # Export variable
```

## Network Commands

### Network Configuration
```bash
# Network interfaces
ip addr show                       # Show IP addresses
ip link show                       # Show network interfaces
ifconfig                           # Network interface configuration (deprecated)
ip route show                      # Show routing table
route -n                           # Show routing table (deprecated)

# Network connectivity
ping hostname                      # Test connectivity
ping -c 4 hostname                 # Ping 4 times only
traceroute hostname                # Trace route to destination
mtr hostname                       # Continuous traceroute
```

### Network Monitoring
```bash
# Network statistics
netstat -tuln                      # Show listening ports
netstat -an                        # Show all connections
ss -tuln                           # Modern replacement for netstat
ss -p                              # Show process names

# Network traffic
iftop                              # Network traffic monitor
nethogs                            # Network usage by process
tcpdump -i interface               # Packet capture
```

### File Transfer
```bash
# Secure copy
scp file user@host:/path           # Copy file to remote host
scp user@host:/path/file .         # Copy file from remote host
scp -r directory user@host:/path   # Copy directory recursively

# Rsync (efficient file synchronization)
rsync -av source/ destination/     # Archive mode with verbose
rsync -av --delete source/ dest/   # Delete files not in source
rsync -av source/ user@host:dest/  # Sync to remote host

# Download files
wget URL                           # Download file
wget -c URL                        # Continue partial download
curl -O URL                        # Download file with curl
curl -L URL                        # Follow redirects
```

## Archive and Compression

### Creating Archives
```bash
# Tar archives
tar -cvf archive.tar files         # Create tar archive
tar -czvf archive.tar.gz files     # Create compressed tar archive (gzip)
tar -cjvf archive.tar.bz2 files    # Create compressed tar archive (bzip2)
tar -cJvf archive.tar.xz files     # Create compressed tar archive (xz)

# Zip archives
zip archive.zip files              # Create zip archive
zip -r archive.zip directory       # Create zip archive recursively
```

### Extracting Archives
```bash
# Extract tar archives
tar -xvf archive.tar               # Extract tar archive
tar -xzvf archive.tar.gz           # Extract gzipped tar archive
tar -xjvf archive.tar.bz2          # Extract bzip2 tar archive
tar -xJvf archive.tar.xz           # Extract xz tar archive
tar -tf archive.tar                # List contents without extracting

# Extract zip archives
unzip archive.zip                  # Extract zip archive
unzip -l archive.zip               # List contents without extracting
```

### Compression Utilities
```bash
# Gzip compression
gzip filename                      # Compress file
gunzip filename.gz                 # Decompress file
zcat filename.gz                   # View compressed file content

# Other compression tools
bzip2 filename                     # Compress with bzip2
bunzip2 filename.bz2               # Decompress bzip2 file
xz filename                        # Compress with xz
unxz filename.xz                   # Decompress xz file
```

## Package Management

### Debian/Ubuntu (APT)
```bash
# Update package lists
sudo apt update                    # Update package database
sudo apt upgrade                   # Upgrade installed packages
sudo apt full-upgrade              # Upgrade with dependency resolution

# Install and remove packages
sudo apt install package_name      # Install package
sudo apt remove package_name       # Remove package
sudo apt purge package_name        # Remove package and config files
sudo apt autoremove                # Remove unused dependencies

# Search and information
apt search keyword                 # Search for packages
apt show package_name              # Show package information
apt list --installed              # List installed packages
apt list --upgradable              # List upgradable packages
```

### Red Hat/CentOS (YUM/DNF)
```bash
# YUM (older systems)
sudo yum update                    # Update all packages
sudo yum install package_name      # Install package
sudo yum remove package_name       # Remove package
yum search keyword                 # Search for packages
yum info package_name              # Show package information

# DNF (newer systems)
sudo dnf update                    # Update all packages
sudo dnf install package_name      # Install package
sudo dnf remove package_name       # Remove package
dnf search keyword                 # Search for packages
dnf info package_name              # Show package information
```

### Snap Packages
```bash
# Snap package management
sudo snap install package_name     # Install snap package
sudo snap remove package_name      # Remove snap package
snap list                          # List installed snaps
snap find keyword                  # Search for snaps
snap refresh                       # Update all snaps
```

## System Administration

### User Management
```bash
# User operations
sudo adduser username              # Add new user (interactive)
sudo useradd username              # Add new user (basic)
sudo userdel username              # Delete user
sudo userdel -r username           # Delete user and home directory
sudo usermod -aG group username    # Add user to group
sudo passwd username               # Change user password

# Group operations
sudo groupadd groupname            # Create new group
sudo groupdel groupname            # Delete group
groups username                    # Show user's groups
id username                        # Show user and group IDs
```

### Service Management (systemd)
```bash
# Service control
sudo systemctl start service      # Start service
sudo systemctl stop service       # Stop service
sudo systemctl restart service    # Restart service
sudo systemctl reload service     # Reload service configuration
sudo systemctl enable service     # Enable service at boot
sudo systemctl disable service    # Disable service at boot

# Service status
systemctl status service          # Show service status
systemctl is-active service       # Check if service is active
systemctl is-enabled service      # Check if service is enabled
systemctl list-units --type=service # List all services
```

### Log Management
```bash
# System logs
journalctl                         # View systemd logs
journalctl -u service_name         # View logs for specific service
journalctl -f                      # Follow logs in real-time
journalctl --since "1 hour ago"    # Logs from last hour
journalctl --until "2023-01-01"    # Logs until specific date

# Traditional log files
tail -f /var/log/syslog            # Follow system log
tail -f /var/log/auth.log          # Follow authentication log
less /var/log/messages             # View system messages
```

### Cron Jobs
```bash
# Cron management
crontab -e                         # Edit user's crontab
crontab -l                         # List user's cron jobs
crontab -r                         # Remove user's crontab
sudo crontab -e -u username        # Edit another user's crontab

# Cron format: minute hour day month weekday command
# Examples:
# 0 2 * * * /path/to/script        # Daily at 2 AM
# */15 * * * * /path/to/script     # Every 15 minutes
# 0 0 1 * * /path/to/script        # First day of every month
```

## Monitoring and Performance

### System Monitoring
```bash
# Real-time monitoring
top                                # Process and system monitor
htop                               # Enhanced process monitor
iotop                              # I/O usage monitor
iftop                              # Network usage monitor
nload                              # Network load monitor

# System statistics
vmstat 1                           # Virtual memory statistics every second
iostat 1                           # I/O statistics every second
sar -u 1 10                        # CPU usage for 10 seconds
mpstat 1                           # Multi-processor statistics
```

### Disk Usage and I/O
```bash
# Disk usage
df -h                              # Filesystem usage
du -sh /path/*                     # Directory sizes
ncdu /path                         # Interactive disk usage analyzer
lsof                               # List open files
lsof /path/to/file                 # Show processes using file

# I/O monitoring
iotop                              # I/O usage by process
iostat -x 1                        # Extended I/O statistics
```

### Memory Analysis
```bash
# Memory usage
free -h                            # Memory usage summary
cat /proc/meminfo                  # Detailed memory information
pmap PID                           # Memory map of process
smem                               # Memory usage with shared memory
```

## Security Commands

### File Security
```bash
# File integrity
md5sum filename                    # Calculate MD5 hash
sha256sum filename                 # Calculate SHA256 hash
sha256sum -c checksums.txt         # Verify checksums

# File attributes
lsattr filename                    # List file attributes
chattr +i filename                 # Make file immutable
chattr -i filename                 # Remove immutable attribute
```

### Network Security
```bash
# Firewall (UFW - Ubuntu)
sudo ufw status                    # Show firewall status
sudo ufw enable                    # Enable firewall
sudo ufw allow 22                  # Allow SSH
sudo ufw allow 80/tcp              # Allow HTTP
sudo ufw deny 23                   # Deny telnet
sudo ufw delete allow 80           # Remove rule

# Firewall (iptables)
sudo iptables -L                   # List rules
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT  # Allow SSH
sudo iptables-save                 # Save rules
```

### System Security
```bash
# User sessions
w                                  # Show logged in users
last                               # Login history
lastlog                            # Last login for all users
who                                # Currently logged in users

# Security logs
sudo tail -f /var/log/auth.log     # Authentication attempts
sudo grep "Failed password" /var/log/auth.log  # Failed login attempts
```

## Best Practices

### Command Line Efficiency
```bash
# History and shortcuts
history                            # Command history
!!                                 # Repeat last command
!n                                 # Repeat command number n
!string                            # Repeat last command starting with string
Ctrl+R                             # Reverse search history
Ctrl+A                             # Move to beginning of line
Ctrl+E                             # Move to end of line
Ctrl+U                             # Clear line before cursor
Ctrl+K                             # Clear line after cursor
Ctrl+L                             # Clear screen
```

### Aliases and Functions
```bash
# Useful aliases (add to ~/.bashrc or ~/.zshrc)
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ..='cd ..'
alias ...='cd ../..'
alias h='history'
alias c='clear'
alias df='df -h'
alias du='du -h'
alias free='free -h'
alias ps='ps auxf'
alias mkdir='mkdir -pv'

# Useful functions
extract() {
    if [ -f $1 ] ; then
        case $1 in
            *.tar.bz2)   tar xjf $1     ;;
            *.tar.gz)    tar xzf $1     ;;
            *.bz2)       bunzip2 $1     ;;
            *.rar)       unrar e $1     ;;
            *.gz)        gunzip $1      ;;
            *.tar)       tar xf $1      ;;
            *.tbz2)      tar xjf $1     ;;
            *.tgz)       tar xzf $1     ;;
            *.zip)       unzip $1       ;;
            *.Z)         uncompress $1  ;;
            *.7z)        7z x $1        ;;
            *)     echo "'$1' cannot be extracted via extract()" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}
```

### Safety Practices
```bash
# Safe practices
alias rm='rm -i'                   # Always prompt before deletion
alias cp='cp -i'                   # Prompt before overwriting
alias mv='mv -i'                   # Prompt before overwriting

# Backup before editing important files
sudo cp /etc/important.conf /etc/important.conf.backup

# Use version control for configuration files
git init /etc
git add /etc/important.conf
git commit -m "Initial configuration"

# Regular backups
rsync -av --delete /home/user/ /backup/user/
```

### Performance Tips
```bash
# Use appropriate tools for the job
# For large files, use:
less instead of cat                # For viewing
head/tail instead of cat           # For partial viewing
grep instead of cat | grep         # For searching

# Pipe efficiently
# Good: grep pattern file | head -10
# Better: grep -m 10 pattern file

# Use find efficiently
find /path -name "*.txt" -exec grep "pattern" {} \;
# Better: find /path -name "*.txt" -exec grep -l "pattern" {} \;

# Monitor resource usage
time command                       # Time command execution
/usr/bin/time -v command          # Detailed timing information
```

### Security Best Practices
```bash
# File permissions
chmod 600 ~/.ssh/id_rsa           # Private key permissions
chmod 644 ~/.ssh/id_rsa.pub       # Public key permissions
chmod 700 ~/.ssh                  # SSH directory permissions

# Secure file editing
umask 077                         # Restrictive default permissions
sudo visudo                       # Edit sudoers file safely
sudo systemctl edit service      # Override service configuration safely

# Regular maintenance
sudo apt update && sudo apt upgrade  # Keep system updated
sudo apt autoremove               # Remove unused packages
sudo apt autoclean                # Clean package cache
```

### Troubleshooting Commands
```bash
# System diagnostics
dmesg | tail                      # Recent kernel messages
journalctl -xe                    # Recent systemd logs with explanations
systemctl --failed                # Show failed services
mount | column -t                 # Show mounted filesystems nicely

# Network troubleshooting
ping -c 4 8.8.8.8                # Test internet connectivity
nslookup domain.com               # DNS lookup
dig domain.com                    # DNS information
netstat -tuln | grep :80          # Check if port 80 is listening

# Process troubleshooting
ps aux | grep process_name        # Find process
lsof -p PID                       # Files opened by process
strace -p PID                     # System calls made by process
```

This comprehensive Linux commands cheatsheet covers essential commands and best practices for system administration, development, and daily usage. Each section includes practical examples and real-world scenarios to help you become more efficient with Linux systems.