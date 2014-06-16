import subprocess
cmd = ["/usr/bin/open", "http://disneyanimation.com"]
subprocess.call(cmd)


cmd = ['/usr/sbin/pkgutil', '--pkgs']
result = subprocess.call(cmd)
print result


cmd = ['/usr/sbin/pkgutil', '--pkgs']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(output, error_output) = proc.communicate()

print "Output:", output

print "Error output:", error_output

print "Return code:", proc.returncode


# don't run this one!
subprocess.call(['/sbin/shutdown', '-r', 'now'])
