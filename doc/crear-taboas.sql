CREATE TABLE "Conta" (
    "IdConta"           TEXT UNIQUE,
    "Nome"              TEXT,
    "Instante Creacion" INTEGER,
    "Descripcion"       TEXT,
    CONSTRAINT contaPK PRIMARY KEY ("IdConta")
);

CREATE TABLE "Divisa" (
    "IdDivisa"                  TEXT UNIQUE,
    "Nome"                      TEXT,
    "Simbolo"                   TEXT,
    "Siglas"                    TEXT,
    "Instante Insercion"        INTEGER,
    "Data Inicio Circulacion"   INTEGER,
    "Tipo"                      String,
    CONSTRAINT divisaPK PRIMARY KEY ("IdDivisa")
);

CREATE TABLE "ValorRelativoDivisa" (
    "IdDivisaAComparar"     TEXT,
    "IdDivisaReferencia"    TEXT,
    "Instante"              INTEGER,
    "ValorUnidade"          FLOAT,
    CONSTRAINT vrdPK PRIMARY KEY ("IdDivisaAComparar", "IdDivisaReferencia"),
    CONSTRAINT vrdFK1 FOREIGN KEY ("IdDivisaAComparar") REFERENCES "Divisa" ("IdDivisa"),
    CONSTRAINT vrdFK2 FOREIGN KEY ("IdDivisaReferencia") REFERENCES "Divisa" ("IdDivisa")    
);

CREATE TABLE "Etiqueta" (
    "IdEtiqueta"        TEXT UNIQUE,
    "Nome"              TEXT,
    "Descripcion"       TEXT,
    "Instante Creacion" TEXT,
    CONSTRAINT etiquetaPK PRIMARY KEY ("IdEtiqueta")
);

CREATE TABLE "Transaccion" (
    "IdTransaccion" TEXT UNIQUE,
    "Instante"      INTEGER,
    "Cantidade"     TEXT,
    "IdDivisa"      TEXT,
    "IdConta"       TEXT,
    "Nome"          TEXT,
    "Notas"         TEXT,
    CONSTRAINT transaccionPK PRIMARY KEY ("IdTransaccion"),
    CONSTRAINT transaccionFK1 FOREIGN KEY ("IdDivisa") REFERENCES "Divisa" ("IdDivisa"),
    CONSTRAINT transacciónFK2 FOREIGN KEY ("IdConta") REFERENCES "Conta" ("IdConta")
);

CREATE TABLE "EtiquetadoTransaccion" (
    "IdEtiqueta"    TEXT,
    "IdTransaccion" TEXT,
    CONSTRAINT etPK PRIMARY KEY ("IdEtiqueta", "IdTransaccion"),
    CONSTRAINT etFK1 FOREIGN KEY ("IdEtiqueta") REFERENCES "Etiqueta" ("IdEtiqueta"),
    CONSTRAINT etFK2 FOREIGN KEY ("IdTransaccion") REFERENCES "Transaccion" ("IdTransaccion")
);
