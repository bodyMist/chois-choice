from django.db import models

# Create your models here.
class Component(models.Model):
    component_id = models.IntegerField(primary_key=True)
    manufacture = models.CharField(max_length=30)
    release = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    data_type = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'component'


class Cpu(models.Model):
    component_component = models.OneToOneField(Component, on_delete=models.CASCADE, primary_key=True)
    socket = models.CharField(max_length=50, blank=True, null=True)
    generation = models.CharField(max_length=50, blank=True, null=True)
    core = models.IntegerField(blank=True, null=True)
    thread = models.IntegerField(blank=True, null=True)
    thickness = models.IntegerField(blank=True, null=True)
    basic_clock = models.CharField(max_length=20, blank=True, null=True)
    max_clock = models.CharField(max_length=20, blank=True, null=True)
    l2_cache = models.CharField(db_column='L2_cache', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l3_cache = models.CharField(db_column='L3_cache', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tdp = models.IntegerField(db_column='TDP', blank=True, null=True)  # Field name made lowercase.
    pcie = models.CharField(db_column='PCIe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    memory_type = models.CharField(max_length=50, blank=True, null=True)
    memory_bus = models.CharField(max_length=50, blank=True, null=True)
    memory_channel = models.IntegerField(blank=True, null=True)
    has_graphic = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cpu'


class Mainboard(models.Model):
    component_component = models.OneToOneField(Component, on_delete=models.CASCADE, primary_key=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    socket = models.CharField(max_length=20, blank=True, null=True)
    chipset = models.CharField(max_length=20, blank=True, null=True)
    chipset_detail = models.CharField(max_length=20, blank=True, null=True)
    cpu_count = models.IntegerField(blank=True, null=True)
    formfactor = models.CharField(max_length=40, blank=True, null=True)
    power = models.CharField(max_length=30, blank=True, null=True)
    memory_type = models.CharField(max_length=30, blank=True, null=True)
    memory_speed = models.CharField(max_length=30, blank=True, null=True)
    memory_slot = models.IntegerField(blank=True, null=True)
    memory_channel = models.IntegerField(blank=True, null=True)
    memory_capacity = models.CharField(max_length=30, blank=True, null=True)
    graphic = models.CharField(max_length=30, blank=True, null=True)
    vga_connect = models.CharField(max_length=20, blank=True, null=True)
    pcie_hex = models.IntegerField(blank=True, null=True)
    pcie_octa = models.IntegerField(blank=True, null=True)
    pcie_quad = models.IntegerField(blank=True, null=True)
    pcie_single = models.IntegerField(blank=True, null=True)
    ssd_slot = models.IntegerField(blank=True, null=True)
    sata_slot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mainboard'

class Memory(models.Model):
    component_component = models.OneToOneField(Component, on_delete=models.CASCADE, primary_key=True)
    device = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    clock = models.CharField(max_length=20, blank=True, null=True)
    timing = models.CharField(max_length=20, blank=True, null=True)
    volt = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'memory'

class Gpu(models.Model):
    component_component = models.OneToOneField(Component, on_delete=models.CASCADE, primary_key=True)
    chipset = models.CharField(max_length=20, blank=True, null=True)
    thickness = models.IntegerField(blank=True, null=True)
    memory_type = models.CharField(max_length=20, blank=True, null=True)
    memory_clock = models.IntegerField(blank=True, null=True)
    memory_capacity = models.CharField(max_length=10, blank=True, null=True)
    hdmi = models.CharField(db_column='HDMI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    displayport = models.CharField(db_column='DisplayPort', max_length=20, blank=True, null=True)  # Field name made lowercase.
    monitor_support = models.IntegerField(blank=True, null=True)
    required_power = models.IntegerField(blank=True, null=True)
    used_power = models.CharField(max_length=20, blank=True, null=True)
    power_port = models.CharField(max_length=20, blank=True, null=True)
    power_case = models.CharField(max_length=20, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    interface = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gpu'


class Hdd(models.Model):
    component_component = models.OneToOneField(Component, on_delete=models.CASCADE, primary_key=True)
    size = models.CharField(max_length=30, blank=True, null=True)
    capacity = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    rpm = models.IntegerField(blank=True, null=True)
    buffer = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hdd'

class Ssd(models.Model):
    component_component = models.OneToOneField(Component, on_delete=models.CASCADE, primary_key=True)
    formfactor = models.CharField(max_length=20, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    capacity = models.CharField(max_length=20, blank=True, null=True)
    seq_read = models.CharField(max_length=20, blank=True, null=True)
    seq_write = models.CharField(max_length=20, blank=True, null=True)
    read_iops = models.IntegerField(blank=True, null=True)
    write_iops = models.IntegerField(blank=True, null=True)
    tbw = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ssd'


class Cooler(models.Model):
    system = models.CharField(max_length=10, blank=True, null=True)
    fan_size = models.CharField(max_length=20, blank=True, null=True)
    fan_thickness = models.IntegerField(blank=True, null=True)
    connector = models.CharField(max_length=20, blank=True, null=True)
    loudness = models.CharField(max_length=30, blank=True, null=True)
    fan_faster = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    tdp = models.IntegerField(blank=True, null=True)
    intel_socket = models.CharField(max_length=100, blank=True, null=True)
    amd_socket = models.CharField(max_length=100, blank=True, null=True)
    component_componenet = models.OneToOneField(Component, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        managed = True
        db_table = 'cooler'


class Power(models.Model):
    type = models.CharField(max_length=20, blank=True, null=True)
    output = models.CharField(max_length=20, blank=True, null=True)
    certification = models.CharField(max_length=50, blank=True, null=True)
    main_cable = models.CharField(max_length=50, blank=True, null=True)
    sub_cable = models.CharField(max_length=50, blank=True, null=True)
    pcie_octa = models.CharField(max_length=20, blank=True, null=True)
    pcie_hexa = models.CharField(max_length=20, blank=True, null=True)
    sata = models.CharField(max_length=20, blank=True, null=True)
    ide = models.CharField(max_length=20, blank=True, null=True)
    component_componenet = models.OneToOneField(Component, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        managed = True
        db_table = 'power'


class Case(models.Model):
    type = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=30, blank=True, null=True)
    compatibility = models.CharField(max_length=100, blank=True, null=True)
    storage = models.IntegerField(blank=True, null=True)
    pci = models.IntegerField(blank=True, null=True)
    fan = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    component_component = models.OneToOneField('Component', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        managed = True
        db_table = 'case'
