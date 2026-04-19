Vagrant.configure("2") do |config|
  #vm1
  config.vm.define "os-linux" do |os|
    os.vm.box = "ubuntu/jammy64"
    os.vm.hostname = "os-linux"
    os.vm.network "private_network", ip: "10.10.10.51"
    os.vm.network "public_network", ip: "192.168.1.51", bridge: "MediaTek Wi-Fi 6 MT7921 Wireless LAN Card"
    os.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 2
    end
  end
  #vm2
  config.vm.define "monitoring" do |mon|
    mon.vm.box = "ubuntu/jammy64"
    mon.vm.hostname = "monitoring"
    mon.vm.network "private_network", ip: "10.10.10.50"
    mon.vm.network "public_network", ip: "192.168.1.50", bridge: "MediaTek Wi-Fi 6 MT7921 Wireless LAN Card"
    mon.vm.provider "virtualbox" do |vb|
      vb.memory = 4096
      vb.cpus = 4
    end
  end
    #vm3
  config.vm.define "webserver" do |web|
    web.vm.box = "ubuntu/jammy64"
    web.vm.hostname = "webserver"
    web.vm.network "private_network", ip: "10.10.10.52"
    web.vm.network "public_network", ip: "192.168.1.52", bridge: "MediaTek Wi-Fi 6 MT7921 Wireless LAN Card"
    web.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 2
    end
  end
end