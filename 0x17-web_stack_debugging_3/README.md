# Web Stack Debugging: Using strace to Fix Apache 500 Error

## Overview

This project involves using `strace` to diagnose and fix a 500 Internal Server Error in Apache running a WordPress site on a LAMP stack. The issue is identified using `strace`, and the fix is automated using Puppet.

## Steps

1. **Use `strace` to Diagnose the Issue:**
   - Attach `strace` to the Apache process and observe the output to identify the cause of the 500 error.

2. **Fix the Issue:**
   - In this example, the issue is a missing PHP module and a conflicting service running on port 80.

3. **Automate the Fix using Puppet:**
   - Create a Puppet manifest to install the missing module and ensure Apache is running without conflicts.

## Puppet Manifest

**`0-strace_is_your_friend.pp`**:

```puppet
# This Puppet manifest installs the missing PHP module and ensures Apache is running.
