<?php
namespace NethServer\Module\Dashboard\Applications;

/**
 * bareos web interface
 *
 * @author stephane de labrusse
 */
class Bareos extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "Bareos";
    }

    public function getInfo()
    {
         $host = explode(':',$_SERVER['HTTP_HOST']);
         return array(
            'url' => "https://".$host[0]."/bareos-webui/",
         );
    }
}
