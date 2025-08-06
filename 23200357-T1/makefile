CC = gcc
CFLAGS = -Wall -O3
LDFLAGS =

EXECUTAVEL = ordena
FONTES = 23200357.c
OBJETOS = $(FONTES:.c=.o)

$(EXECUTAVEL): $(OBJETOS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

run: $(EXECUTAVEL)
	./$(EXECUTAVEL) $(TAMANHO)

clean:
	rm -f $(EXECUTAVEL) $(OBJETOS)

.PHONY: run clean
