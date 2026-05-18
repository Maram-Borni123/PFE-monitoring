Vagrant.configure("2") do |config|
  #vm1
  config.vm.define "os-linux" do |os|
    os.vm.box = "ubuntu/jammy64"
    os.vm.hostname = "os-linux"
    os.vm.network "private_network", ip: "10.10.10.51"
    os.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
      vb.cpus = 1
    end
  end
  #vm2
  config.vm.define "monitoring" do |mon|
    mon.vm.box = "ubuntu/jammy64"
    mon.vm.hostname = "monitoring"
    mon.vm.network "private_network", ip: "10.10.10.50"
    mon.vm.provider "virtualbox" do |vb|
      vb.memory = 3072
      vb.cpus = 2
    end
  end
    #vm3
  config.vm.define "webserver" do |web|
    web.vm.box = "ubuntu/jammy64"
    web.vm.hostname = "webserver"
    web.vm.network "private_network", ip: "10.10.10.52"
    web.vm.provider "virtualbox" do |vb|
      vb.memory = 1536
      vb.cpus = 1
    end
  end
  #vm4
  config.vm.define "database" do |data|
    data.vm.box = "ubuntu/jammy64"
    data.vm.hostname = "database"
    data.vm.network "private_network", ip: "10.10.10.53"
    data.vm.provider "virtualbox" do |vb|
      vb.memory = 1536
      vb.cpus = 1
    end
  end
  #vm5
  config.vm.define "nosql" do |ns|
    ns.vm.box = "ubuntu/jammy64"
    ns.vm.hostname = "nosql"
    ns.vm.network "private_network", ip: "10.10.10.54"
    ns.vm.provider "virtualbox" do |vb|
      vb.memory = 1536
      vb.cpus = 1
    end
  end
  #vm6
  config.vm.define "appjava" do |aj|
    aj.vm.box = "ubuntu/jammy64"
    aj.vm.hostname = "appjava"
    aj.vm.network "private_network", ip: "10.10.10.55"
    aj.vm.provider "virtualbox" do |vb|
      vb.memory = 2048
      vb.cpus = 2
    end
  end
  #vm7
  config.vm.define "appscript" do |as|
    as.vm.box = "ubuntu/jammy64"
    as.vm.hostname = "appscript"
    as.vm.network "private_network", ip: "10.10.10.56"
    as.vm.provider "virtualbox" do |vb|
      vb.memory = 1536
      vb.cpus = 1
    end
  end
  #vm8
  config.vm.define "application-services" do |inf|
    inf.vm.box = "ubuntu/jammy64"
    inf.vm.hostname = "application-services"
    inf.vm.network "private_network", ip: "10.10.10.57"
    inf.vm.provider "virtualbox" do |vb|
      vb.memory = 2048 
      vb.cpus = 2
    end
  end
end