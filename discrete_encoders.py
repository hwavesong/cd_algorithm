import numpy as np

import torch


class CDBinEncoder():
    def __init__(self, g, r):  # g is the original input dimension, and r is the target dimension
        super(object, self).__init__()

        self.fix_seed(37)

        print('initia parameters... ...')
        self.g = g
        self.r = r

        self.V = torch.from_numpy(self.generate_V(g, g * 5)).float().cuda()
        self.normed_V = (self.V / torch.norm(self.V, dim=0).unsqueeze(0)).cuda()

        self.P = self.generate_P_svd(self.V, r).float().cuda()

        self.V_p = (self.P @ self.V * np.sqrt(r)).float().cuda()
        self.inverse_V_p = torch.pinverse(self.V_p).float().cuda()

    def fix_seed(self, seed):
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)

    def generate_V(self, num_rows, num_cols):
        limit = np.sqrt(2. / (num_rows + num_cols))
        random_matrix = np.random.normal(loc=0.0, scale=limit, size=(num_rows, num_cols))

        emb_mean = np.mean(random_matrix, axis=0)[None, :]
        random_matrix -= emb_mean

        return random_matrix

    def generate_P_svd(self, V, r):
        u, sigma, v = torch.svd(V)
        return u[:r, :]

    def generate_P(self, g, r):
        limit = np.sqrt(6. / (g + r))
        random_matrix = np.random.uniform(low=-limit, high=limit, size=(g, r))

        u, sigma, v = np.linalg.svd(random_matrix)

        return u[:r, :]

    def dcd(self, S, U, V):
        L = U.shape[0]
        Q = (V @ S.t()).cuda()

        while True:
            is_update = False
            for i in range(L):
                U_b_prime = torch.cat((U[:i, :], U[i + 1:, :]))

                v_p = V[i, :]
                V_p_prime = torch.cat((V[:i, :], V[i + 1:, :]))

                q = Q[i, :]

                bracket_result = (q - U_b_prime.t() @ V_p_prime @ v_p).cuda()

                new_u = bracket_result.sign().cuda()
                new_u[torch.eq(new_u, 0.)] = 1.

                if torch.all(torch.eq(new_u, U[i, :])):
                    continue
                U[i, :] = new_u
                is_update = True

            if not is_update: break

        return U.t().cpu().numpy()

    def encode(self, X):
        X = torch.from_numpy(X).cuda()

        normed_X = (X / torch.norm(X, dim=1).unsqueeze(1)).cuda()

        S = (normed_X @ self.normed_V * self.r).cuda()

        X_small_code = (S @ self.inverse_V_p).cuda()

        return self.dcd(S, X_small_code.t(), self.V_p)
