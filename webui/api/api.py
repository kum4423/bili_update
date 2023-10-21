# (C) 2019-2020 lifegpc
# This file is part of bili.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from .. import web, apilogincheck
from . import getapilist, InvalidInputEroor
from .session import NotLoginError
from json import dumps
import traceback

apil = getapilist()


class api:
    def GET(self, t):
        web.header('Content-Type', 'text/json; charset=utf-8')
        h = web.cookies().get('section')
        if apilogincheck(h):
            return dumps({'code': -403})
        asc = False
        if web.input().get('asc') is not None:
            asc = True
        for i in apil:
            try:
                e = i(t)
                return dumps(e._handle(), ensure_ascii=asc)
            except InvalidInputEroor:
                pass
            except NotLoginError:
                return {'code': -501}
            except Exception:
                return dumps({'code': -500, 'e': traceback.format_exc()}, ensure_ascii=asc)
        return dumps({'code': -404})
