/* vxi11_cmd.c
 * Copyright (C) 2006 Steve D. Sharples
 *
 * A simple interactive utility that allows you to send commands and queries to
 * a device enabled with the VXI11 RPC ethernet protocol. Uses the files
 * generated by rpcgen vxi11.x, and the vxi11_user.h user libraries.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 * 
 * The author's email address is steve.sharples@nottingham.ac.uk
 */

#include "vxi11_user.h"
#include "unescape.h"
#define BUF_LEN 100000

int a_to_i(char *s, int *value) {
    if ( s != NULL && *s != '\0' && value != NULL )
    {
        char *endptr = s;
        *value = (int)strtol(s, &endptr, 10);
        if ( *endptr == '\0' )
        {
            return 1;
        }
    }
    return 0; /* failed to convert string to integer */
}

unsigned long long millisecondsSinceEpoch() {
  struct timeval t;
  gettimeofday(&t, NULL);
  return (unsigned long long)(t.tv_sec) * 1000 +
    (unsigned long long)(t.tv_usec) / 1000;
}

int	main(int argc, char *argv[]) {

static char	*device_ip;
static char	*device_name;
char            cmd[256];
char		buf[BUF_LEN];
int		ret;
int             read_timeout;
long		bytes_returned;
CLINK		*clink;
unsigned long long s_time, e_time;

	clink = new CLINK;

	if (argc < 5) {
		printf("usage: %s your.inst.ip.addr device_name timeout/msec command\n",argv[0]);
		exit(1);
		} else {
                
          device_ip = argv[1];
          device_name = argv[2];
          //read_timeout = atoi(argv[3]);
          if (!a_to_i(argv[3], &read_timeout)) {
            fprintf(stderr, "wrong read_timeout value!\n");
            exit(1);
          }
          ret = vxi11_open_device(device_ip,clink,device_name);
          if (ret != 0) {
          fprintf(stderr, "Error: could not open device %s, quitting\n",device_ip);
          exit(2);
          }
        }

        memset(buf, 0, BUF_LEN);	// initialize buffer
        
        strcpy(cmd, unescape(argv[4]));
        
        //fprintf(stderr, " cmd: %s%s%s", ">>>", cmd, "<<<\n\n");
        
        //exit(0);

        s_time = millisecondsSinceEpoch();
        
        if (vxi11_send(clink, cmd) < 0) {
          //
          ret=vxi11_close_device(device_ip,clink);
          exit(3);
        }
        
        bytes_returned = vxi11_receive(clink, buf, BUF_LEN, read_timeout);

        e_time = millisecondsSinceEpoch();
        
        if ((read_timeout > 0) && (bytes_returned > 0) || (read_timeout == 0) && (strlen(buf) > 0)) {
          printf("%llu|%s|%llu", s_time, buf, e_time);
          //printf("%s", buf);
        }

        ret=vxi11_close_device(device_ip,clink);

    return 0;
	}
