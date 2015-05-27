#! /bin/bash

fbcmd FQL "SELECT uid, name, friend_count FROM user WHERE uid = me() OR uid IN (SELECT uid2 FROM friend WHERE uid1 = me()) AND friend_count!=0"

