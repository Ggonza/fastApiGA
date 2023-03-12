from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Uuid, String, Boolean, LargeBinary
from config.db import meta, engine


roles = Table("roles", meta,
              Column("id", Uuid, primary_key=True),
              Column("name", String(255)),
              Column("description", String(255))
              )

users = Table("users", meta,
              Column("id", Uuid),
              Column("username", String(255)),
              Column("first_name", String(255)),
              Column("last_name", String(255)),
              Column("dni", String(255)),
              Column("phone", String(255)),
              Column("email", String(255)),
              Column("password", String(255)),
              Column("created_at", String(255)),
              Column("updated_at", String(255)),
              Column("is_active", Boolean),
              Column("is_superuser", Boolean),
              Column("is_blocked", Boolean),
              Column("last_login", String(255)),
              Column("date_joined", String(255)),
              Column("avatar", LargeBinary),
              Column("role", Uuid, ForeignKey("roles.id"))
              )

role = relationship("Role", backref="users")


meta.create_all(engine)
