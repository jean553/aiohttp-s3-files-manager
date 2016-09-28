# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 expandtab :

PROJECT = "aiohttp-s3-files-manager"

DOCKER_ENV = {
  "HOST_USER_UID" => Process.euid,
  "S3_ENDPOINT" => "http://s3:5000",
  "BUCKET_NAME" => "mybucket",
  "S3_ACCESS_KEY" => "dummy_value_cannot_be_none",
  "S3_SECRET_ACCESS" => "dummy_value_cannot_be_none",
  "APP_PATH" => "/home/vagrant/aiohttp-s3-files-manager",
  "VIRTUAL_ENV_PATH" => "/tmp/virtual_env35",
  "ENV_NAME" => "devdocker"
}

ENV['VAGRANT_NO_PARALLEL'] = 'yes'
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'docker'
Vagrant.configure(2) do |config|

  config.vm.define "s3" do |s3|
    s3.vm.provider "docker" do |d|
      d.image = "jean553/docker-s3-server-dev"
      d.name = "#{PROJECT}_s3"
    end
  end

  config.ssh.insert_key = false
  config.vm.define "dev", primary: true do |app|
    app.vm.provider "docker" do |d|
      d.image = "allansimon/allan-docker-dev-python"
      d.name = "#{PROJECT}_dev"
      d.link "#{PROJECT}_s3:s3"
      d.has_ssh = true
      d.env = DOCKER_ENV
      d.volumes =  [
        "#{ENV['PWD']}/:#{DOCKER_ENV['APP_PATH']}",
      ]
    end
    app.ssh.username = "vagrant"

    # Note: we're using a shell to launch ansible
    # instead of directly using the `ansible_local` because of this
    # http://stackoverflow.com/questions/37989742
    app.vm.provision "local_ansible", type: "shell" do |s|
      s.env = DOCKER_ENV
      s.inline = "
        set -e
        cd $APP_PATH
        ansible-playbook provisionning/bootstrap-dev.yml
        echo 'done, you can now run `vagrant ssh dev`'
      "
    end
  end
end
