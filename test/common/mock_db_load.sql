-- fyle_load_tpa_export_batches
insert into
fyle_load_tpa_export_batches ("id", "name", "success", "exported_at", "url")
values
('exbtCGWmKieHip' , 'DB-Connector-Test-1', 'True', '2020-01-01T00:00:00.000Z', 'haha.com');

insert into
fyle_load_tpa_export_batches ("id", "name", "success", "exported_at", "url")
values
('exbt0EdBt3ojED' , 'DB-Connector-Test-2', 'True', '2020-02-01T00:00:00.000Z', 'test.com');

-- fyle_load_tpa_export_batch_lineitems
insert into
fyle_load_tpa_export_batch_lineitems ("batch_id", "object_id", "object_type", "reference")
values (?, ?, ?, ?) ,
('exbtCGWmKieHip', 'set7HcqxEGR4e', 'SETTLEMENT', 'P/2019/11/R/1');
insert into
fyle_load_tpa_export_batch_lineitems ("batch_id", "object_id", "object_type", "reference")
values (?, ?, ?, ?) ,
('exbt0EdBt3ojED', 'setNLmVl57sEd', 'SETTLEMENT', 'P/2019/11/R/7');
