<?php
echo $_GET['callback']. "(". json_encode($_SERVER['REMOTE_ADDR']). ")";
