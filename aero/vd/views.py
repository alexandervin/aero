import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
import subprocess

from vd.models import AdvUser


def index(request):
    command_view = ['bash' + os.path.join('lsblk')]
    process = subprocess.Popen(command_view, stdout=subprocess.PIPE)
    output_view = process.stdout
    script_format = subprocess.run(["mkfs", "ext4", "/dev/sdb1"])
    script_mount = subprocess.run(["mount", "-v", "-t", "ext4", "/dev/sdb1"])
    script_umount = subprocess.run(["umount", "/dev/sdb1"])
    return render(request, 'vd/index.html', {"output_view": output_view, "script_umount": script_umount,
                                             "script_format": script_format, "script_mount": script_mount})


class VDLoginView(LoginView):
    template_name = 'vd/login.html'


class VDLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'vd/logout.html'


@login_required
def profile(request):
    bbs = AdvUser.objects.filter(author=request.user.pk)
    context = {'bbs': bbs}
    return render(request, 'vd/profile.html', context)
