#!/usr/bin/python
# encoding: utf-8
"""
mirrortool.py

Created by Greg Neagle on 2013-06-05.

A PyObjC port of Fabian Canas's command-line mirror tool from
http://mirror-displays.googlecode.com/

See:

https://developer.apple.com/library/mac/#documentation/graphicsimaging/reference/Quartz_Services_Ref/Reference/reference.html

https://developer.apple.com/library/mac/#documentation/graphicsimaging/Conceptual/QuartzDisplayServicesConceptual/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004316
"""

import sys
import os

import Quartz


def main():
    # default mode if none specified
    mode = 'query'

    # get our own name
    toolname = os.path.basename(sys.argv[0])

    # get any mode that may have been passed at the command line
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()

    # make sure the mode is one we know about
    if not mode in ['toggle', 'on', 'off', 'query', 'help']:
        mode = 'help'

    if mode == 'help':
        print """Usage: %s [toggle|on|off|query|help]
    toggle: Toggle mirroring mode
    on:     Turn mirroring on
    off:    Turn mirroring off
    query:  Return mirroring state to stdout (default)
    help:   Print this message and exit.""" % toolname
        exit(0)

    # we currently know only how to handle two attached displays
    max_displays = 2

    # get active display list
    # CGGetActiveDisplayList:
    #     Provides a list of displays that are active (or drawable).
    (err, active_displays,
     number_of_active_displays) = Quartz.CGGetActiveDisplayList(
                                                    max_displays, None, None)
    if err:
        print >> sys.stderr, "Error in obtaining active display list: %s" % err
        exit(-1)

    # get online display list
    # CGGetOnlineDisplayList:
    #     Provides a list of displays that are online
    #     (active, mirrored, or sleeping).
    (err, online_displays,
     number_of_online_displays) = Quartz.CGGetOnlineDisplayList(
                                                    max_displays, None, None)
    if err:
        print >> sys.stderr, "Error in obtaining online display list: %s" % err
        exit(-1)

    # make sure we have the right number of displays.
    # currently that number is exactly 2.
    if number_of_online_displays > 2:
        print >> sys.stderr, (("Cannot handle more than two displays. "
                              "%s displays detected.")
                              % number_of_online_displays)
        exit(-1)

    if number_of_online_displays < 2:
        print >> sys.stderr, (("Can't mirror fewer than two displays. "
                              "%s displays detected.")
                              % number_of_online_displays)
        exit(-1)

    if number_of_online_displays == 2:
        if online_displays[0] == Quartz.CGMainDisplayID():
            secondary_display = online_displays[1]
        else:
            secondary_display = online_displays[0]

    if mode == 'query':
        if number_of_active_displays == 2:
            print 'Display mirroring is off'
        else:
            print 'Display mirroring is on'
        exit(0)

    # begin display configuration
    (err, config_ref) = Quartz.CGBeginDisplayConfiguration(None)
    if err:
        print >> sys.stderr, "Error with CGBeginDisplayConfiguration: %s" % err
        exit(-1)

    if mode == 'toggle':
        if number_of_active_displays == 2:
            # currently unmirrored
            err = Quartz.CGConfigureDisplayMirrorOfDisplay(
                config_ref, secondary_display, Quartz.CGMainDisplayID())
        else:
            # currently mirrored
            err = Quartz.CGConfigureDisplayMirrorOfDisplay(
                config_ref, secondary_display, Quartz.kCGNullDirectDisplay)

    if mode == 'on':
        if number_of_active_displays == 2:
            # currently unmirrored
            err = Quartz.CGConfigureDisplayMirrorOfDisplay(
                config_ref, secondary_display, Quartz.CGMainDisplayID())

    if mode == 'off':
        if number_of_active_displays != 2:
            # currently mirrored
            err = Quartz.CGConfigureDisplayMirrorOfDisplay(
                config_ref, secondary_display, Quartz.kCGNullDirectDisplay)

    if err:
        print >> sys.stderr, "Error configuring displays: %s" % err
        exit(-1)

    # apply the changes
    err = Quartz.CGCompleteDisplayConfiguration(
                                config_ref, Quartz.kCGConfigurePermanently)
    if err:
        print >> sys.stderr, ("Error with CGCompleteDisplayConfiguration: %s"
                              % err)
        exit(-1)


if __name__ == '__main__':
    main()